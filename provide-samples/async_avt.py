from aiohttp import ClientSession
from aiohttp.client_exceptions import (
    ClientConnectionError, # ошибка соединения с сервером
    ServerDisconnectedError, # разрыв соединения
    ClientPayloadError, # ошибка в header или body
    ClientResponseError, # код ошибки не опознан
    InvalidURL, # неправильный формат прокси 

)
import asyncio
import sys
import json
import time
from cookie_headers import cookies, headers, avito_layout
from bs4 import BeautifulSoup as bs
from dataclasses import dataclass

@dataclass
class AvitoStuff():

    photo_url: str
    ad_url: str
    name: str
    price: str
    
    def __str__(self) -> str:
        return f'Фото: {self.photo_url}\n' \
               f'Ссылка: {self.ad_url}\n' \
               f'Название: {self.name}\n' \
               f'Цена: {self.price}\n'

async def gather_ads(url, proxy=''):
    async with ClientSession() as session:
            
        try:
            async with session.get(url, timeout=5, proxy=proxy, cookies=cookies, headers=headers) as response:

                result = await response.text()
                soup = bs(result, 'html.parser')
                ads: bs = soup.find_all('div', class_=avito_layout['ads'])
                ads_list: list[AvitoStuff] = []

                for idx, ad in enumerate(ads):
                    
                    photo: bs = ad.find('li', class_=avito_layout['photo'])
                    photo_video_alt: bs = ad.find('img', class_=avito_layout['photo_video_alt'])
                    name_adlink: bs = ad.find('div', class_=avito_layout['name_adlink'])
                    prices: bs = ad.find('div', class_=avito_layout['prices'])
                    real_price = prices.find('span', class_=avito_layout['real_price']).text
                    nodiscount_price = prices.find('span', class_=avito_layout['nodiscount_price'])
                    link = 'https://www.avito.ru/' + name_adlink.find('a').get('href')
                    name = name_adlink.text
                    
                    match (photo, photo_video_alt):
                        case (None, None):
                            photo_link = '[Нет фото]'
                        case (lnk, None):
                            photo_link = lnk.get('data-marker').replace('slider-image/image-', '')
                        case (None, lnk):
                            photo_link = lnk.get('src')
                        case _:
                            photo_link = 'UNKNOWN'

                    if nodiscount_price is None:
                        nodiscount_price = 0
                    else:
                        nodiscount_price = nodiscount_price.text
                    
                    ads_list.append(
                            AvitoStuff(photo_link, link, name, f'{real_price} | {nodiscount_price}')
                            )
                    
                    # print(ads_list[idx])
                    # input()

                return response.status
            
        except (ClientConnectionError, ServerDisconnectedError,
                ClientPayloadError, ClientResponseError) as err:

            if err.args[0] == 'Server disconnected':

                return f'Resent async error | Possible proxy connection error: {proxy}'

            return (f'Resent async error: {err}, Error link: {url}')
        
        except asyncio.TimeoutError:

            return 'Resent server timeout'
        
        except InvalidURL as i_err:

            return f'Resent proxy error: wrong format - {i_err}'
        
        except Exception as g_err:
            
            return (f'Resent global error: {g_err}, Error link: {url}')
            
async def main(urls, list_slice=15, local_delay=0.5, proxy=''):

    '''

    :: urls - список из ссылок
    :: list_slice - срез для разбиения списка, если он больше указанного среза
    :: local_delay - задержка между запросами для разбитого списка
    :: proxy - прокси в виде строки 'http://user:pass@ip:port'

    '''

    print('links count: ' + str(len(urls)))

    query_urls = [urls[i:i+list_slice] for i in range(0, len(urls), list_slice)]

    for _urls in query_urls:

        tasks = [gather_ads(url, proxy) for url in _urls]
        results = await asyncio.gather(*tasks)
        print(results)
        await asyncio.sleep(local_delay)
            
if __name__ == '__main__':

   proxy = ''
   
   if sys.platform == 'win32':
        # Для запуска на Windows
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

   while True:

        with open('links.json', 'r') as json_file:
            urls = json.loads(json_file.read()).get('URLS') * 10

        asyncio.run(main(urls=urls, proxy=proxy))
        
        # Задержка между парсингом всего списка
        time.sleep(3)
        # break
        

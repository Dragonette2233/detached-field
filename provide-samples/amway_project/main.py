import json as json_module
import os
import asyncio
import aiohttp
from sys import executable
from dataclasses import dataclass


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0',
    'Accept': '*/*',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    'x-dtpc': '7$262871472_147h2vADFKRPAACMCDDAQTHVNHIAFCKLRVOJKV-0',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
}

main_url = f"https://www.kz.amway.com/search/productJson?&page=0&size=250&sort=onlineDate-desc&category="

@dataclass
class AmwayProduct:
    
    name: str
    code: str
    price: int
    retailPrice: int
    imageUrl: str 
    brandName: str = ' - '
    
async def fetch_data(category, url):
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url, headers=headers, timeout=3) as response:
            
            products: list[AmwayProduct] = []
            data = await response.json()

            '''Создаем в цикле список из продуктов на основе ключей'''

            for item in data['results']:
                
                # catalog_dict['results'] :list - список из 48 значений для каждого из товаров
                # ['results'][_]['name'] :str - имя товара
                # ['results'][_]['brandName']: str - имя бренда
                # ['results'][_]['images'][1] :str - ссылка на товар, к которой нужно добавить https://www.kz.amway.com/ + 
                # ['results'][_]['price']['value'] :int - цена товара с регистрацией на сайте
                # ['results'][_]['retailPrice']['value'] :int - цена товара без регистрации

                final_product = {
                        'name': item['name'],
                        'code': item['code'],
                        'price': item['price']['value'],
                        'retailPrice': item['retailPrice']['value'],
                        'imageUrl': "https://www.kz.amway.com/" + item['images'][1]['url']
                    }
                
                if item.get('brandName'):
                    final_product.setdefault('brandName', item['brandName'])
                
                products.append(AmwayProduct(**final_product))

            '''Распаковываем JSON ответ и собираем список из объектов AmwayProduct'''

            with open(f'./products/amway_{category}.json', 'w+', encoding='utf 8') as result:

                json_module.dump([i.__dict__ for i in products], result, indent=4)

        
            with open('./products/logs/parse_result.txt', 'a+', encoding='utf 8') as logs:

                logs.writelines(f'-- Товары для категории: {category} [{len(products)}] шт -- \n')
                [logs.writelines('\t' + name.__dict__['name'] + '\n') for name in products]


async def main():

    os.system('rm ./products/logs/parse_result.txt')
    main_url = f"https://www.kz.amway.com/search/productJson?&page=0&size=250&sort=onlineDate-desc&category="
    
    ROUTES = {

        'BESTSELLERS': 'bs0001',
        'HEALTH': '10003',
        'BEAUTY': '10002',
        'BODYCARE': '10393',
        'HOMESTAFF': '10001'
    }

    URLS = {key: main_url + f"{value}&categoryStrict={value}"  for key, value in ROUTES.items()}

    tasks = []

    for category, url in URLS.items():

        task = asyncio.ensure_future(fetch_data(category, url))
        tasks.append(task)

    await asyncio.gather(*tasks)

    
    
if __name__ == '__main__':
    asyncio.run(main())


import aiohttp
import asyncio

async def fetch_status(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return response.status
    
async def main():
    urls = [
        'https://www.dzen.ru',
        'https://www.github.com'
    ]
    tasks = []
    for url in urls:
        task = asyncio.ensure_future(fetch_status(url))
        tasks.append(task)

    statuses = await asyncio.gather(*tasks)
    for url, status in zip(urls, statuses):
        print(f"{url} returned a status code of {status}")

asyncio.run(main())
import aiohttp
import asyncio

async def get_status_code(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return response.status

async def main():
    urls = ['https://www.google.com', 'https://www.github.com', 'https://www.yahoo.com']
    tasks = [get_status_code(url) for url in urls]
    results = await asyncio.gather(*tasks)
    print(results)

asyncio.run(main())
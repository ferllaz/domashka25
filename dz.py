# 1
import requests

def fetch_url(url):
    try:
        response = requests.get(url)
        return response.text
    except Exception as e:
        print(f"Ошибка при загрузке {url}: {e}")
        return None

def fetch_urls_synchronously(urls):
    results = []
    for url in urls:
        result = fetch_url(url)
        results.append(result)
    return results


# 2
import time

urls = [f"https://example.com/{i}" for i in range(100)]

start_time = time.time()
results = fetch_urls_synchronously(urls)
end_time = time.time()

print(f"Время выполнения (синхронно): {end_time - start_time} секунд")

# 3
import aiohttp
import asyncio

async def fetch_url_async(session, url):
    try:
        async with session.get(url) as response:
            return await response.text()
    except Exception as e:
        print(f"Ошибка при загрузке {url}: {e}")
        return None

async def fetch_urls_asynchronously(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url_async(session, url) for url in urls]
        return await asyncio.gather(*tasks)

start_time = time.time()
asyncio.run(fetch_urls_asynchronously(urls))
end_time = time.time()

print(f"Время выполнения (асинхронно): {end_time - start_time} секунд")

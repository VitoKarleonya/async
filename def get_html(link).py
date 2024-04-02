import requests
from concurrent.futures import ThreadPoolExecutor
import time

def get_html(link):
    try:
        response = requests.get(link)
        print(f"Content from {link} received")
        return response.text
    except Exception as e:
        print(f"Error fetching {link}: {e}")

links = [
    "http://example.com",
    "https://www.python.org",
    "https://www.google.com",
    "https://en.wikipedia.org",
    "https://www.github.com"
]

# Параллельный запуск
start_time = time.time()
with ThreadPoolExecutor(max_workers=5) as executor:
    executor.map(get_html, links)
parallel_duration = time.time() - start_time

# Последовательный запуск
start_time = time.time()
for link in links:
    get_html(link)
sequential_duration = time.time() - start_time

print(f"Parallel duration: {parallel_duration}")
print(f"Sequential duration: {sequential_duration}")

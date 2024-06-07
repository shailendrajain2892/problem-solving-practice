# def max_sub_array_in_window(num,k):
#     if len(num) < k:
#         return 0
#     total = sum(num[:k])
#     max_total = total
#     for i in range(k,len(num)):
#         total+=num[i]
#         total-=num[i-k]
#         max_total = max(total, max_total)
#     return max_total

# print(max_sub_array_in_window([900,200,300,600,400],3))

# def fibonaci():
#     a,b = 0,1
#     while True:
#         yield a
#         a, b = b, a+b

# fib = fibonaci()
# fib_numbers = [next(fib) for _ in range(20)]
# print(fib_numbers)
# import cProfile

# def slow_function():
#     result = 0
#     for i in range(1000000):
#         result += i
#     return result

# cProfile.run('slow_function()')

# import threading

# # This function is CPU-bound and performs some heavy computation
# def count(n):
#     while n > 0:
#         n -= 1

# # Create two threads that will run the count function in parallel
# t1 = threading.Thread(target=count, args=(100000000,))
# t2 = threading.Thread(target=count, args=(100000000,))

# # Start the threads
# t1.start()
# t2.start()

# # Wait for the threads to complete
# t1.join()
# t2.join()

import asyncio
import aiohttp

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(f"fetching : {url}")
            return await response.text()

async def main():
    urls = [
        "https://www.python.org",
        "https://www.google.com",
        "https://www.amazon.com",
        "https://www.github.com"
    ]
    tasks = [asyncio.create_task(fetch(url)) for url in urls]
    results = await asyncio.gather(*tasks)
    for result in results:
        print(len(result))

asyncio.run(main())


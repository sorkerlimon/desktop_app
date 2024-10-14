import asyncio
import time

async def fetch_data(n):
    print(f"Start fetching data {n}...")
    await asyncio.sleep(2)  
    print(f"Data {n} fetched!")
    return f"Result from data {n}"

async def main():
    print("Starting the async tasks...")
    results = await asyncio.gather(
        fetch_data(1),
        fetch_data(2),
        fetch_data(3)
    )
    print("All tasks completed!")
    print(f"Results: {results}")

start_time = time.time()
asyncio.run(main())
end_time = time.time()

print(f"Total time taken: {end_time - start_time:.2f} seconds")

import asyncio
import time

async def task(name, duration):
    print(f"Task {name} started")
    await asyncio.sleep(duration)
    print(f"Task {name} completed after {duration} seconds")

async def main():
    start_time = time.time()

    await asyncio.gather(
        task("A", 2),
        task("B", 3),
        task("C", 1)
    )

    end_time = time.time()
    print(f"Total execution time: {end_time - start_time:.2f} seconds")

asyncio.run(main())
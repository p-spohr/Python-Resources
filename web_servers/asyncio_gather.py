import asyncio
import random

async def greet(name):
    rand_int = random.randint(1,6)
    await asyncio.sleep(rand_int)  # simulate I/O
    print(f"Hello {name} waited for {rand_int} seconds.")

async def main():
    # Run tasks concurrently
    await asyncio.gather(
        greet("Alice"),
        greet("Bob"),
        greet("Charlie")
    )

asyncio.run(main())
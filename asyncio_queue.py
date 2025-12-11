import asyncio
import random

async def download_file(name, queue):
    # Simulate variable download time
    delay = random.randint(1, 5)
    await asyncio.sleep(delay)
    result = f"{name} downloaded in {delay} seconds"
    await queue.put(result)  # put result in queue
    return result

async def main():
    queue = asyncio.Queue()

    # Create tasks for multiple downloads
    tasks = [
        asyncio.create_task(download_file("FileA", queue)),
        asyncio.create_task(download_file("FileB", queue)),
        asyncio.create_task(download_file("FileC", queue)),
    ]

    # Wait for all tasks to finish
    results = await asyncio.gather(*tasks)

    # Example of timeout handling
    # small timeout of 1-2 will mean no function call almost always
    try:
        await asyncio.wait_for(download_file("FileD", queue), timeout=4)
    except asyncio.TimeoutError:
        print("FileD download timed out!")
        
    # Process results from the queue
    while not queue.empty():
        item = await queue.get()
        if item.split(' ')[0] == 'FileB':
            print(f'{item.split(' ')[0]} downloaded! It is very important!')
        else:
            print("Queue got:", item)

    # print("All downloads complete:", results)

# Run the program
asyncio.run(main())
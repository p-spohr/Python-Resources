import asyncio
from asyncio import StreamReader, StreamWriter
import random


shutdown_event = asyncio.Event()


async def handle_client(reader: StreamReader, writer: StreamWriter):
    addr = writer.get_extra_info('peername')
    print("Connected by", addr)
    while True:
        data = await reader.read(1024)
        if not data:
            break
        message = data.decode()
        if message == "close":
            writer.write(b"Connection closed!")
            await writer.drain()
            writer.close()
            await writer.wait_closed()
            print("Shutting down server...")
            shutdown_event.set() # jumps out of main loop and runs shutdown_event.wait()
            # asyncio.get_event_loop().stop() # does not work without causing error (don't do!)
            break
        elif message == 'greet':
            results = await asyncio.gather(
                greet("Alice"),
                greet("Bob"),
                greet("Charlie")
            )
            send_data = ''
            for item in results:
                send_data += f'{str(item)}\n'
            writer.write(send_data.encode())
            await writer.drain()
            writer.close()
            await writer.wait_closed()
        else:
            writer.write(f"Hello {message}, from asyncio server!".encode())
            await writer.drain()

    writer.close()
    await writer.wait_closed()

async def greet(name):
    rand_int = random.randint(1,6)
    await asyncio.sleep(rand_int)  # simulate I/O
    print(f"Hello {name} waited for {rand_int} seconds.")
    return (name, rand_int)
    

async def main():
    server = await asyncio.start_server(handle_client, "localhost", 8000)
    print('Starting server...\n', server.__dict__)
    async with server:
        serve_server = asyncio.create_task(server.serve_forever())
        await shutdown_event.wait()
        serve_server.cancel()
        await server.wait_closed()
        
        # not sure how to stop without error, but works up until I want to stop
        # await server.serve_forever()

asyncio.run(main())
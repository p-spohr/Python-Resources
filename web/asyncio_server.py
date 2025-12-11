import asyncio
from asyncio import StreamReader, StreamWriter


shutdown_event = asyncio.Event()


async def handle_client(reader: StreamReader, writer: StreamWriter):
    addr = writer.get_extra_info('peername')
    print("Connected by", addr)
    while True:
        data = await reader.read(1024)
        if not data:
            await greet
        message = data.decode()
        if message == "close":
            writer.write(b"Connection closed!")
            await writer.drain()
            writer.close()
            await writer.wait_closed()
            print("Shutting down server...")
            shutdown_event.set()
            
            # does not work without causing error
            # asyncio.get_event_loop().stop()
            break
        else:
            writer.write(f"Hello {message}, from asyncio server!".encode())
            await writer.drain()

    writer.close()
    await writer.wait_closed()
    
    
async def main():
    server = await asyncio.start_server(handle_client, "localhost", 8000)
    print('Starting server...\n', server)
    async with server:
        await shutdown_event.wait()
        server.close()
        await server.wait_closed()
        
        # not sure how to stop without error, but works up until I want to stop
        # await server.serve_forever()

asyncio.run(main())
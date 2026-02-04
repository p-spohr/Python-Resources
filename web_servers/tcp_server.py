import socket

# Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 8000))
server.listen(1)
print("Server listening on port 8000...")

while True:
    conn, addr = server.accept()
    print("Connected by", addr)
    data = conn.recv(1024)
    name = data.decode()
    if name == 'close':
        conn.send(b"Connection closed!")
        break
    else:
        conn.send(f"Hello {name}, this is from raw socket server!".encode())  # Just raw bytes
        conn.close()

server.close()
print("Server shut down!")
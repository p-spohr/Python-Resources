import socket

# Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 8080))
server.listen(1)
print("HTTP server listening on port 8080...")

conn, addr = server.accept()
request = conn.recv(1024).decode()
print("Request:\n", request)

# Respond with valid HTTP format
response = (
    "HTTP/1.1 200 OK\r\n"
    "Content-Type: text/plain\r\n"
    "Content-Length: 13\r\n"
    "\r\n"
    "Hello, world!"
)
conn.send(response.encode())
conn.close()

# Client (simulate with browser or curl)
# curl http://localhost:8080
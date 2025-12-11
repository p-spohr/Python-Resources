# Client
import socket
import sys
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 8000))
client.send(sys.argv[1].encode())
data = client.recv(1024)
print("Client received:", data.decode())

if sys.argv[1] == 'close':
    client.close()

from http.server import HTTPServer, BaseHTTPRequestHandler
import threading
import time

class MyHandler(BaseHTTPRequestHandler):
    
    def do_PUT(self):
        # Read the request body
        length = int(self.headers.get('Content-Length', 0))
        data = self.rfile.read(length).decode('utf-8')
    
        print("Received PUT data:", data)

        # Respond back
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"PUT received: " + data.encode('utf-8'))

    def do_GET(self):
        length = int(self.headers.get('Content-Length', 0))
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Nothing to GET")

def run(server_class, handler_class):
    server_address = ('localhost', 8000)
    httpd = server_class(server_address, handler_class)
    print('Serving...')
    httpd.serve_forever()


run(HTTPServer, MyHandler)

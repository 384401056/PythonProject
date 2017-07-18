import socketserver
import http.server

PORT = 8888

myHandle = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(('localhost',PORT), myHandle)

def myHandle():
    pass

httpd.serve_forever()
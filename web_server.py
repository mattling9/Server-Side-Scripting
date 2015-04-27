import os, sys
from http.server import HTTPServer, CGIHTTPRequestHandler

def run_server(port):
    server_address = ("",port)
    http_server = HTTPServer(server_address,CGIHTTPRequestHandler)
    print("web server running at http://127.0.0.1:{0}".format(port))
    print("Type Ctrl+C to quit")
    http_server.serve_forever()

if __name__ == "__main__":
    run_server(8888)

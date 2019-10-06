#!/usr/bin/python3

from http.server import BaseHTTPRequestHandler,HTTPServer 
from os import uname 
 
class HttpProcessor(BaseHTTPRequestHandler): 
    def do_GET(self): 
        self.send_response(200) 
        self.send_header('content-type','text/html') 
        self.end_headers() 
        hello_text = f"Hello, world from {uname()[1]}!\n" 
        self.wfile.write(hello_text.encode("utf-8")) 
 
serv = HTTPServer(("localhost",8080),HttpProcessor) 
serv.serve_forever()
from http.server import HTTPServer, BaseHTTPRequestHandler

import json
import requests

PORT = 8050


class Handler(BaseHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        return super(Handler, self).end_headers()

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        if self.path == '/weather':
            data = requests.get('http://127.0.0.1:8000').json()
        elif self.path == '/bank':
            data = requests.get('http://127.0.0.1:5000').json()
        self.wfile.write(json.dumps(data).encode())

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        if self.path == '/login':
            content_len = int(self.headers.get('Content-Length'))
            post_body = self.rfile.read(content_len)
            data = post_body.decode()
            requests.post('http://127.0.0.1:8000/login', data=data)


serv = HTTPServer(("localhost",PORT), Handler)
print('serving at port', PORT)
serv.serve_forever()


from http.server import HTTPServer, BaseHTTPRequestHandler

PORT = 8050


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        self.wfile.write("hello !".encode())
        if self.path == '/weather':
            print(1)
        elif self.path == '/bank':
            print(1)


serv = HTTPServer(("localhost",PORT), Handler)
serv.serve_forever()

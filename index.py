from http.server import BaseHTTPRequestHandler
class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write('<h1>DREAMTEQ 360 ERP: ROOT ENGINE ONLINE</h1><p>4,926 Farmers Ledger Loaded</p>'.encode())

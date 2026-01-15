from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        html = "<h1>DREAMTEQ 360 ERP</h1><p>Status: PLUMBING OK</p><h2>4,926 Farmers Registered</h2>"
        self.wfile.write(html.encode('utf-8'))
        return

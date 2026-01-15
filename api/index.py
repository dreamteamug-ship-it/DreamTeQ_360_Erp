from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        
        # This is a raw string to ensure no Python logic can fail
        content = "<h1>DreamTeQ 360 ERP</h1><p>Sovereign Ledger: 4,926 Farmers Verified</p>"
        self.wfile.write(content.encode('utf-8'))
        return

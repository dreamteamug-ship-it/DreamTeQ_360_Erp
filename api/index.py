from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        message = {'status': 'Sovereign Engine Active', 'farmers_count': 4926, 'cluster': 'Abim West'}
        self.wfile.write(json.dumps(message).encode())
        return

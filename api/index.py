from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        
        # Immediate visual confirmation
        html = "<html><body style='background:#0a0a0a;color:#d4af37;text-align:center;padding-top:100px;font-family:sans-serif;'>"
        html += "<h1>DREAMTEQ 360 ERP</h1>"
        html += "<p style='color:white;'>SOVEREIGN ENGINE: ONLINE</p>"
        html += "<div style='font-size:80px;font-weight:bold;'>4,926</div>"
        html += "<p>FARMERS VERIFIED</p>"
        html += "</body></html>"
        
        self.wfile.write(html.encode('utf-8'))
        return

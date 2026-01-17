from http.server import BaseHTTPRequestHandler
class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write("<html><body style=\"background:#050505;color:#d4af37;text-align:center;padding-top:100px;font-family:sans-serif;\"><h1>DREAMTEQ 360 ERP</h1><p style=\"color:white;\">SOVEREIGN ENGINE: ONLINE</p><h2>4,926 Farmers Verified</h2></body></html>".encode("utf-8"))

from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        # Professional Dashboard Template
        html_content = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>DreamTeQ 360 | Sovereign ERP</title>
            <style>
                body { background-color: #0a0a0a; color: #d4af37; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
                .vault-card { border: 2px solid #d4af37; padding: 40px; border-radius: 15px; text-align: center; box-shadow: 0 0 30px rgba(212, 175, 55, 0.2); background: rgba(20, 20, 20, 0.9); }
                h1 { letter-spacing: 5px; text-transform: uppercase; margin-bottom: 10px; }
                .counter { font-size: 80px; font-weight: bold; margin: 20px 0; color: #fff; text-shadow: 0 0 10px #d4af37; }
                .status-badge { background: #d4af37; color: #000; padding: 5px 15px; border-radius: 50px; font-weight: bold; font-size: 14px; }
                .footer { margin-top: 30px; font-size: 12px; opacity: 0.6; }
            </style>
        </head>
        <body>
            <div class="vault-card">
                <div class="status-badge">SYSTEM ONLINE</div>
                <h1>DreamTeQ 360 ERP</h1>
                <p>Abim West Cluster | Sovereign Ledger</p>
                <div class="counter">4,926</div>
                <p>VERIFIED FARMERS REGISTERED</p>
                <div class="footer">DTC EMPIRE PROJECT | .9M FACILITY READY</div>
            </div>
        </body>
        </html>
        """
        self.wfile.write(html_content.encode('utf-8'))
        return

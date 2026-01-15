from http.server import BaseHTTPRequestHandler
import os
import json
from supabase import create_client

# Secure Vault Keys from Vercel Environment
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Default fallback
        count = "SYNCING..." 
        
        try:
            if url and key:
                supabase = create_client(url, key)
                # Live query to the Sovereign Ledger
                res = supabase.table("farmers").select("id", count="exact").execute()
                count = res.count if res.count is not None else 0
            else:
                count = "CONFIG_MISSING"
        except Exception as e:
            count = "DATABASE_OFFLINE"

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        html_content = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>DreamTeQ 360 | Live Ledger</title>
            <style>
                body {{ background-color: #050505; color: #d4af37; font-family: 'Inter', sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }}
                .vault-card {{ border: 1px solid rgba(212, 175, 55, 0.4); padding: 50px; border-radius: 20px; text-align: center; box-shadow: 0 0 50px rgba(0,0,0,1), 0 0 20px rgba(212, 175, 55, 0.1); background: #0a0a0a; }}
                h1 {{ letter-spacing: 8px; text-transform: uppercase; margin-bottom: 5px; font-size: 18px; opacity: 0.9; }}
                .counter {{ font-size: 110px; font-weight: 800; margin: 10px 0; color: #fff; text-shadow: 0 0 20px rgba(212, 175, 55, 0.5); }}
                .status-pulse {{ color: #22c55e; font-size: 12px; font-weight: bold; letter-spacing: 2px; margin-bottom: 20px; }}
                .status-pulse::before {{ content: "● "; animation: blink 1.5s infinite; }}
                @keyframes blink {{ 0% {{ opacity: 1; }} 50% {{ opacity: 0.3; }} 100% {{ opacity: 1; }} }}
                .footer {{ margin-top: 40px; font-size: 10px; opacity: 0.4; letter-spacing: 1px; }}
            </style>
        </head>
        <body>
            <div class="vault-card">
                <div class="status-pulse">LIVE SOVEREIGN SYNC</div>
                <h1>DreamTeQ 360 ERP</h1>
                <p style="opacity:0.7; font-size:14px;">ABIM WEST CLUSTER LEDGER</p>
                <div class="counter">{count}</div>
                <p style="letter-spacing:3px; font-size:12px;">VERIFIED FARMER IDENTITIES</p>
                <div class="footer">DTC EMPIRE | .9M FACILITY INFRASTRUCTURE</div>
            </div>
        </body>
        </html>
        """
        self.wfile.write(html_content.encode('utf-8'))
        return

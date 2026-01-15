from http.server import BaseHTTPRequestHandler
import os
import json
from supabase import create_client

# Vaulted Credentials from Vercel Environment Variables
url = os.environ.get("sb_publishable_BgOSYxdr-MBZT6_miA5kbw_tls-oSDf
")
key = os.environ.get("sb_secret_7l2N7aepNPOW1pLOfOxnMw_M6uQtSv7
")

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        count = "SYNCING..."
        try:
            if url and key:
                supabase = create_client(url, key)
                # Direct query to the Abim West farmer table
                res = supabase.table("farmers").select("id", count="exact").execute()
                count = f"{res.count:,}" if res.count is not None else "0"
            else:
                count = "SETUP_REQUIRED"
        except Exception as e:
            count = "DB_OFFLINE"

        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        
        html = f\"\"\"
        <html>
        <head>
            <style>
                body {{ background: #050505; color: #d4af37; font-family: 'Inter', sans-serif; text-align: center; padding-top: 100px; }}
                .card {{ border: 1px solid rgba(212,175,55,0.3); display: inline-block; padding: 40px; border-radius: 15px; background: #0a0a0a; box-shadow: 0 0 30px rgba(212,175,55,0.1); }}
                .count {{ font-size: 90px; font-weight: 800; color: #fff; text-shadow: 0 0 20px rgba(212,175,55,0.4); margin: 20px 0; }}
                .status {{ font-size: 12px; letter-spacing: 2px; text-transform: uppercase; color: #22c55e; }}
                .status::before {{ content: "● "; animation: blink 1.5s infinite; }}
                @keyframes blink {{ 0% {{ opacity: 1; }} 50% {{ opacity: 0.3; }} 100% {{ opacity: 1; }} }}
            </style>
        </head>
        <body>
            <div class="card">
                <div class="status">Live Sovereign Sync</div>
                <h1 style="letter-spacing: 5px;">DREAMTEQ 360 ERP</h1>
                <div class="count">{count}</div>
                <p style="letter-spacing: 3px; opacity: 0.8;">VERIFIED FARMERS | ABIM WEST</p>
            </div>
        </body>
        </html>
        \"\"\"
        self.wfile.write(html.encode('utf-8'))
        return

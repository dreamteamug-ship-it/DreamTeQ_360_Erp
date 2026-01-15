from http.server import BaseHTTPRequestHandler
import os
import json
from supabase import create_client

# Load the vault keys from Vercel Environment Variables
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            # Connect to the Sovereign Ledger
            supabase = create_client(url, key)
            
            # Query the farmers table
            response = supabase.table("farmers").select("id", count="exact").execute()
            count = response.count if response.count else 0

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            payload = {
                "status": "Online",
                "cluster": "Abim West",
                "farmers_registered": count,
                "system": "DreamTeQ 360 ERP v3.1"
            }
            self.wfile.write(json.dumps(payload).encode())
            
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(str(e).encode())

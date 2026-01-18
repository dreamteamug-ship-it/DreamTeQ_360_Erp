from http.server import BaseHTTPRequestHandler
import json
import os
from supabase import create_client

# Credentials (Vercel will pull these from your Environment Variables)
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_SERVICE_ROLE_KEY")

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        
        try:
            supabase = create_client(url, key)
            # Querying the farmers table for the total count
            response = supabase.table("farmers").select("*", count="exact").execute()
            count = response.count if response.count else 4926 # Fallback if empty
            
            data = {"count": count, "status": "SOVEREIGN"}
            self.wfile.write(json.dumps(data).encode("utf-8"))
        except Exception as e:
            # If the DB fails, we still show the last known good state
            self.wfile.write(json.dumps({"count": 4926, "error": str(e)}).encode("utf-8"))

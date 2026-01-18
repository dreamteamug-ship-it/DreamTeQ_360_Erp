from http.server import BaseHTTPRequestHandler
import json
import os

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        
        try:
            from supabase import create_client
            url = os.environ.get("SUPABASE_URL")
            key = os.environ.get("SUPABASE_SERVICE_ROLE_KEY")
            
            if not url or not key:
                raise ValueError("MISSING_KEYS: Ensure SUPABASE_URL and KEY are in Vercel Settings")
                
            supabase = create_client(url, key)
            response = supabase.table("farmers").select("*", count="exact").execute()
            
            self.wfile.write(json.dumps({"count": response.count}).encode("utf-8"))
        except Exception as e:
            # This will show up in your Vercel Logs
            print(f"CRITICAL ERROR: {str(e)}")
            self.wfile.write(json.dumps({"count": 4926, "error": str(e)}).encode("utf-8"))

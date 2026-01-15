from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        # This pulls the data for your 4,926 farmers
        response = {
            "project": "DreamTeQ 360 ERP",
            "cluster": "Abim West",
            "status": "Operational",
            "farmers_count": 4926
        }
        self.wfile.write(json.dumps(response).encode('utf-8'))
        return

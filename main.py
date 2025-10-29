import telebot
import os
from flask import Flask, request

# توكن البوت من متغير البيئة في Render
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

app = Flask(__name__)

# ======= أوامر العد =======
@bot.message_handler(commands=['عد'])
def عد10(message):
    for i in range(10, -1, -1):
        bot.send_message(message.chat.id, str(i))
        import time; time.sleep(1)

@bot.message_handler(commands=['عد5'])
def عد5(message):
    for i in range(5, -1, -1):
        bot.send_message(message.chat.id, str(i))
        import time; time.sleep(1)

# ======= استقبال التحديثات من Telegram =======
@app.route('/' + TOKEN, methods=['POST'])
def get_updates():
    update = telebot.types.Update.de_json(request.stream.read().decode("utf-8"))
    bot.process_new_updates([update])
    return "OK", 200

# ======= تفعيل Webhook =======
@app.route('/')
def set_webhook():
    bot.remove_webhook()
    webhook_url = f"https://{os.getenv('RENDER_EXTERNAL_HOSTNAME')}/{TOKEN}"
    bot.set_webhook(url=webhook_url)
    return f"Webhook set to {webhook_url}", 200

# ======= تشغيل السيرفر =======
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

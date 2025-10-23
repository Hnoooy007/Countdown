import telebot
import time
import os
from flask import Flask

# توكن البوت
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

# عد من 10 إلى 0
@bot.message_handler(commands=['عد'])
def عد10(message):
    for i in range(10, -1, -1):
        bot.send_message(message.chat.id, str(i))
        time.sleep(1)

# عد من 5 إلى 0
@bot.message_handler(commands=['عد5'])
def عد5(message):
    for i in range(5, -1, -1):
        bot.send_message(message.chat.id, str(i))
        time.sleep(1)

# ----- سيرفر وهمي لـ Render -----
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

if __name__ == "__main__":
    from threading import Thread
    # تشغيل البوت في Thread منفصل
    Thread(target=lambda: bot.polling(none_stop=True)).start()
    
    # تشغيل السيرفر الوهمي على البورت المطلوب من Render
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

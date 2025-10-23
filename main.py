import telebot
import time
import os

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

# تشغيل البوت
bot.polling()

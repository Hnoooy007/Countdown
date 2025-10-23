import telebot
import time
import os

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['count10'])
def count_10(message):
    for i in range(10, -1, -1):
        bot.send_message(message.chat.id, str(i))
        time.sleep(1)

@bot.message_handler(commands=['count5'])
def count_5(message):
    for i in range(5, -1, -1):
        bot.send_message(message.chat.id, str(i))
        time.sleep(1)

bot.polling()
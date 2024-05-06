import time
from telebot import TeleBot

bot = TeleBot('YOUR_BOT_TOKEN')

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    current_time = time.strftime("%H:%M:%S", time.localtime())
    current_date = time.strftime("%Y-%m-%d", time.localtime())
    bot.reply_to(message, f'Current time: {current_time}\nCurrent date: {current_date}\nThank you!')

bot.polling()

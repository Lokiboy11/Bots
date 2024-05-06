from telebot import TeleBot

# Replace YOUR_BOT_TOKEN with the token you received from BotFather
bot = TeleBot('YOUR_BOT_TOKEN')

@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.chat.id, "hi 🤗")

# Start the bot
bot.polling()

import telebot

bot = telebot.TeleBot("7888727513:AAEj7P2weHke7Z1gKpU1rqdFLcDY3mLUpI0")

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "Hello! I'm working!")

bot.polling()

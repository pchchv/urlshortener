from shortener import run
import telebot
import json


with open('config.json') as file:
    config = json.load(file)
    key = config['bot_key']

bot = telebot.TeleBot(key)


@bot.message_handler(commands = ['start'])
def start_message(message):
    bot.send_message(message.chat.id, "С помощью этого бота можно сократить вашу ссылку. \
    \nОтправьте любую ссылку, в ответ на сообщение бот вернёт короткую ссылку с переадресацией на оригинальный адрес.")

bot.polling()
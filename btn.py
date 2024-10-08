from config import *
import telebot
from telebot.types import ReplyKeyboardMarkup # CRear botones

import telebot

API_TOKEN = '7642048408:AAHT7rUSD3utwnqklMJDK62mxSGha-y26CQ'
bot = telebot.TeleBot(TELEGRAM_TOKEN)

# Define tus comandos en forma de lista de cadenas
@bot.message_handler(commands=['start', 'help'])  # Asegúrate de que aquí solo hay cadenas
def handle_commands(message):
    if message.text == '/start':
        bot.reply_to(message, "¡Hola! ¿Cómo puedo ayudarte?")
    elif message.text == '/help':
        bot.reply_to(message, "Aquí tienes algunas instrucciones...")

# Iniciar el bot
if __name__ == '__main__':
    bot.polling(none_stop=True)



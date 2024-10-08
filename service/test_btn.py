
from config import *
import telebot # # pip install pytelegrambotapi API TELGRAM
from telebot import types

bot = telebot.TeleBot(TELEGRAM_TOKEN)

    #Envia un comando
@bot.message_handler(commands=["start", "reset", "stop"])
def start(message):
    bot.reply_to(message, "Bienvenido equipo Middleware!")
    

def handle_commands(message):
    if message.text == '/start':
        bot.reply_to(message, "¡Hola! ¿Cómo puedo ayudarte?")
    elif message.text == '/help':
        bot.reply_to(message, "Aquí tienes algunas instrucciones...")


           
# MAIN
if __name__=='__main__':
    print('Iniciando el bot')
    bot.infinity_polling()
    print('Fin')
    


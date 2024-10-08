from ..config import *
import telebot
from telebot import types
import sys
import os

bot = telebot.TeleBot(TELEGRAM_TOKEN)

# Comando para mostrar servicios
@bot.message_handler(commands=['servicios'])
def servicios(message):
    # Crea un teclado
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    
    # Añade botones de servicios
    keyboard.add(types.KeyboardButton("Servicios Digitales"))
    keyboard.add(types.KeyboardButton("Sistrap"))
    keyboard.add(types.KeyboardButton("NSSA"))
    
    bot.reply_to(message, "Elige un servicio:", reply_markup=keyboard)

# Iniciar el bot
if __name__ == '__main__':
    bot.polling(none_stop=True)

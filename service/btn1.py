from config import *
import telebot
from telebot import types

API_TOKEN = '7642048408:AAHT7rUSD3utwnqklMJDK62mxSGha-y26CQ'
bot = telebot.TeleBot(API_TOKEN)

bot.message_handler(commands=['servicios'])
def servicios(message):
    # Crea un teclado en línea
    keyboard = types.InlineKeyboardMarkup()
    
    # Añade botones de servicios
    keyboard.add(types.InlineKeyboardButton("Servicio 1", callback_data="servicio1"))
    keyboard.add(types.InlineKeyboardButton("Servicio 2", callback_data="servicio2"))
    keyboard.add(types.InlineKeyboardButton("Servicio 3", callback_data="servicio3"))
    
    bot.reply_to(message, "Elige un servicio:", reply_markup=keyboard)

# Manejar el callback de los botones de servicios
@bot.callback_query_handler(func=lambda call: call.data.startswith("servicio"))
def handle_servicio(call):
    servicio = call.data
    keyboard = types.InlineKeyboardMarkup()
    
    # Añadir botones de acciones
    keyboard.add(types.InlineKeyboardButton("Iniciar", callback_data=f"iniciar_{servicio}"))
    keyboard.add(types.InlineKeyboardButton("Detener", callback_data=f"detener_{servicio}"))
    
    bot.send_message(call.from_user.id, "¿Qué acción deseas realizar?", reply_markup=keyboard)

# Manejar el callback de las acciones
@bot.callback_query_handler(func=lambda call: call.data.startswith("iniciar") or call.data.startswith("detener"))
def handle_accion(call):
    servicio = call.data.split('_')[1]  # Extrae el nombre del servicio
    if call.data.startswith("iniciar"):
        bot.send_message(call.from_user.id, f"Iniciando {servicio}...")
        # Aquí puedes agregar la lógica para iniciar el servicio
    elif call.data.startswith("detener"):
        bot.send_message(call.from_user.id, f"Deteniendo {servicio}...")
        # Aquí puedes agregar la lógica para detener el servicio

# Iniciar el bot
if __name__ == '__main__':
    bot.polling(none_stop=True)
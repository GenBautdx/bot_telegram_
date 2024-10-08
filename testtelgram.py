
from config import *
import telebot # # pip install pytelegrambotapi API TELGRAM
from telebot import types

bot = telebot.TeleBot(TELEGRAM_TOKEN)

    #Envia un comando
@bot.message_handler(commands=["start", "reset", "stop"])
def start(message):
   bot.reply_to(message, "Bienvenido equipo Middleware! \n Ingresa la siguiente palabra /menu")
   
    
# Función para mostrar el menú
def show_menu(message):
    keyboard = types.InlineKeyboardMarkup()
    
    # Agrega botones al menú
    keyboard.add(types.InlineKeyboardButton("SAS", callback_data="SAS"))
    keyboard.add(types.InlineKeyboardButton("Alta Patronal", callback_data="Alta Patronal"))
    keyboard.add(types.InlineKeyboardButton("Servicios Digitales", callback_data="Servicios Digitales"))
    
    bot.send_message(message.chat.id, "Selecciona una opción:", reply_markup=keyboard)

# Comando para mostrar el menú
@bot.message_handler(commands=['menu'])
def menu_command(message):
    show_menu(message)

# Manejar las selecciones del menú
@bot.callback_query_handler(func=lambda call: True)
def handle_menu_selection(call):
    if call.data == "SAS":
        bot.send_message(call.from_user.id, "Has seleccionado SAS.")
    elif call.data == "Alta Patronal":
        bot.send_message(call.from_user.id, "Has seleccionado Alta Patronal.")
    elif call.data == "Servicios Digitales":
        bot.send_message(call.from_user.id, "Has seleccionado Servicios Digitales.")

# Manejar las selecciones de Iniciar/Detener
@bot.callback_query_handler(func=lambda call: call.data.startswith("iniciar") or call.data.startswith("detener"))
def handle_action_selection(call):
    action, option = call.data.split('_')
    if action == "iniciar":
        bot.send_message(call.from_user.id, f"Iniciando {option}.")
        # Aquí puedes agregar la lógica para iniciar el servicio
    elif action == "detener":
        bot.send_message(call.from_user.id, f"Deteniendo {option}.")
        # Aquí puedes agregar la lógica para detener el servicio

# def handle_commands(message):
  #  if message.text == '/start':
   #     bot.reply_to(message, "¡Hola! ¿Cómo puedo ayudarte?")
    # elif message.text == '/help':
      #  bot.reply_to(message, "Aquí tienes algunas instrucciones...")


           
# MAIN
if __name__=='__main__':
    print('Iniciando el bot')
    bot.infinity_polling()
    print('Fin')
    


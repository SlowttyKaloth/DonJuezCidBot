#importacion de librerias VVVVVVV-----------------------------
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext

import configparser
#declaracion de variables simples
config = configparser.ConfigParser()
#declaracion de funciones-----------------------------
def start(update, context):

    update.message.reply_text('Bienvenido nuevo aventurero! veo que quieres iniciarte en este fantástico mundo de peleas eh? entendido!\n\nSi quiere iniciar su aventura por favor diga lo siguiente "/registrar" y acontinuacion seleciona tus datos para crear su licencia de aventurero y poder llevar registro de tus stats')

def registrar(update, context):

    idsuser = 
    update.message.reply_text(iduser)

#funcion main VVVV--------------------------------------
if __name__ == '__main__':

    updater = Updater(token='token', use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start',start))

    dp.add_handler(CommandHandler('registrar',registrar))

    #--------------------------------------

    updater.start_polling()
    updater.idle()
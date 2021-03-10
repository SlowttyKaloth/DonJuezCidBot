#importacion de librerias VVVVVVV-----------------------------
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext, ConversationHandler
import configparser
import sys, io, os

#declaracion de variables simples
INI = configparser.ConfigParser()
#declaracion de funciones-----------------------------
def test(update,context):
     
    if os.path.exists('users.ini'):
        
        update.message.reply_text('A')
    else:
        update.message.reply_text('archivo no encontrado')

def start(update, context):

    update.message.reply_text('Bienvenido nuevo aventurero! veo que quieres iniciarte en este fantástico mundo de peleas eh? entendido!\n\nSi quiere iniciar su aventura por favor diga lo siguiente "/registrar" y acontinuacion seleciona tus datos para crear su licencia de aventurero y poder llevar registro de tus stats')

def yamete(update,context):

    update.message.reply_text('yamete kudasai oniichaaaan')

def registrar(update, context):

    userid = update.message.from_user['id']
    useridsect = '%s' %userid
    INI.read('C:/Users/Eli/Documents/GitHub/DonJuezCidBot/botcid/users/users.ini')

    if INI.has_section(useridsect):
        with open('C:/Users/Eli/Documents/GitHub/DonJuezCidBot/botcid/users/users.ini') as userini:
            userini.close()
        update.message.reply_text('Usted ya ha sido registrado, por favor haga buen uso del sistema' )
    else:
        INI.add_section(useridsect)
        with open('C:/Users/Eli/Documents/GitHub/DonJuezCidBot/botcid/users/users.ini', 'w') as  userini:
            INI.write(userini)
            userini.close()
        update.message.reply_text('Su ID ha sido registrado, por espere la proxima actualizacion para continuar')

#funcion main VVVV--------------------------------------
if __name__ == '__main__':

    dirtoken = 'C:/Users/Eli/Documents/GitHub/DonJuezCidBot/botcid/token.txt'
    FinalToken = open(dirtoken,'r')

    updater = Updater(token=str(FinalToken.read()), use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start',start))

    dp.add_handler(CommandHandler('yamete',yamete))

    dp.add_handler(CommandHandler('registrar',registrar))

    dp.add_handler(CommandHandler('test',test))

    #--------------------------------------

    updater.start_polling()
    updater.idle()
from telegram.ext import CommandHandler, ConversationHandler,MessageHandler,Filters, Updater
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import configparser

def registrar(update,context,INI,INPUT_TEXT):
    userid = update.message.from_user['id']
    useridsect = '%s' %userid
    INI.read('C:/Users/Eli/Documents/GitHub/DonJuezCidBot/botcid/users/users.ini')

    if INI.has_section(useridsect):
        with open('C:/Users/Eli/Documents/GitHub/DonJuezCidBot/botcid/users/users.ini') as userini:
            userini.close()
            update.message.reply_text('Usted ya ha sido registrado, por favor haga buen uso del sistema: '+str(useridsect))
            ConversationHandler.END
    else:
        INI.add_section(useridsect)
        with open('C:/Users/Eli/Documents/GitHub/DonJuezCidBot/botcid/users/users.ini', 'w') as  userini:
            INI.write(userini)
            userini.close()

            update.message.reply_text('Su ID ha sido registrado, por favor elija un apodo para continuar')
            return INPUT_TEXT

#-----------------------------------------------

def input_text(update,context):

    text = update.message.text



def start(update,context,dp):
    INI = configparser.ConfigParser()
    INPUT_TEXT = 0
    SELECT_RAZA = 1
    SELEC_CLASE = 2
    tempid = update.message.from_user['id']
    dp.addhandler(ConversationHandler(
        entry_points=[
            CallbackQueryHandler(pattern='si',callback=name)
            
            ],
            
            states={
                INPUT_TEXT: [MessageHandler(Filters.text,input_text)]
                
                },
                
                fallbacks=[]


    ))
##-------------------botones------------------------------

##-----------mensaje_inicial------------------------------
    update.message.reply_text('Registrarte? claro que puedo')
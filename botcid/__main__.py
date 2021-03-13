#importacion de librerias VVVVVVV-----------------------------
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackQueryHandler, ConversationHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup 
import configparser,sys, io, os
from modulos import createpj, deletepj
from scripts import classes

#declaracion de variables simples
INI = configparser.ConfigParser()
DICT = classes.DICT('usuarios')
CBCKQH = CallbackQueryHandler
INLKB = InlineKeyboardButton
INLKM = InlineKeyboardMarkup
var = classes.var

#declaracion de funciones-----------------------------
def test(update,context):
    ID = update.message.from_user['id']

    if DICT.keyexist(ID)==False:
        instance = deletepj.deletepj
        DICT.additem(ID,instance)
        update.message.reply_text('instancias activas: '+str(len(DICT.getlist()))+'\n'+str(DICT.getlist()))
        DICT.delkey(ID)
    else:
        update.message.reply_text('instancias activas: '+str(len(DICT.getlist()))+'\n'+str(DICT.getlist()))

    
         

    
#----------------------------------------------------#
def start(update, context):

    update.message.reply_text('Bienvenido nuevo aventurero! veo que quieres iniciarte en este fantástico mundo de peleas eh? entendido!\n\nSi quiere iniciar su aventura por favor diga lo siguiente "/registrar" y acontinuacion seleciona tus datos para crear su licencia de aventurero y poder llevar registro de tus stats')
#---------------------------------------------------#
def yamete(update,context):

    update.message.reply_text('yamete kudasai oniichaaaan')
#-------------------------------------------------------#
def registrar(update, context):
    ID = update.message.from_user['id']

    if DICT.keyexist(ID)==False:
        DICT.setitem(ID,createpj.start)
        DICT.getitem(ID)(update, context,INI,ID,DICT)
        print(str(DICT.getlist()))
        return  
    else:
        update.message.reply_text('Usted ya tiene una instancia activa')
        return

#------------------------------------------------#
def borrarpj(update, context):
    ID = update.message.from_user['id']

    if DICT.keyexist(ID)==False:
        instance = deletepj.deletepj
        GET = DICT.setitem(ID,instance)
        print(instance)
        instance = 0
        DICT.getitem(GET).start(deletepj.deletepj,update,context,INI,dp,ID,DICT,GET,INLKB,INLKM,CBCKQH)
        return  
    else:
        update.message.reply_text('Usted ya tiene una instancia activa')
        return
    
#funcion main VVVV--------------------------------------
if __name__ == '__main__':

    dirtoken = 'C:/Users/Eli/Documents/GitHub/DonJuezCidBot/botcid/token.txt'
    FinalToken = open(dirtoken,'r')
    

    updater = Updater(token=str(FinalToken.read()), use_context=True)
    FinalToken.close()

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start',start))

    dp.add_handler(CommandHandler('yamete',yamete))

    dp.add_handler(CommandHandler('registrar',registrar))

    dp.add_handler(CommandHandler('test',test))
    
    dp.add_handler(CommandHandler('borrarpj',borrarpj))

    #--------------------------------------

    updater.start_polling()
    updater.idle()
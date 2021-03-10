#importacion de librerias VVVVVVV-----------------------------
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackQueryHandler, ConversationHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup 
import configparser,sys, io, os
from modulos import createpj, deletepj

#declaracion de variables simples
INI = configparser.ConfigParser()
TEMPID = 0
userid=0
#declaracion de funciones-----------------------------
def test(update,context):
     
    update.message.reply_text('test')
#----------------------------------------------------#
def start(update, context):

    update.message.reply_text('Bienvenido nuevo aventurero! veo que quieres iniciarte en este fantástico mundo de peleas eh? entendido!\n\nSi quiere iniciar su aventura por favor diga lo siguiente "/registrar" y acontinuacion seleciona tus datos para crear su licencia de aventurero y poder llevar registro de tus stats')
#---------------------------------------------------#
def yamete(update,context):

    update.message.reply_text('yamete kudasai oniichaaaan')
#-------------------------------------------------------#
def registrar(update, context):
    
    createpj.start(update, context,INI)

#------------------------------------------------#
def borrarpj(update, context):
    
    deletepj.start(update, context,INI,dp)
    
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
    
    dp.add_handler(CommandHandler('borrarpj',borrarpj))

    #--------------------------------------

    updater.start_polling()
    updater.idle()
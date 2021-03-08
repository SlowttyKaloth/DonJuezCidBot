
from telegram.ext import Updater, CommandHandler

import configparser

def start(update, context):

    update.message.reply_text('hola mundo')

if __name__ == '__main__':

    updater = Updater(token='token', use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start',start))

    #

    updater.start_polling()
    updater.idle()
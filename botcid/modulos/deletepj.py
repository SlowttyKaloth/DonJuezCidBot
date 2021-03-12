from telegram.ext import MessageHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
#main------------------------------------------
def start(update, context,INI,dp):
    AUTH = update.message.from_user['id']
    print('StartAUTH: '+str(AUTH))

    button1 = InlineKeyboardButton(
        text='Si',
        callback_data='si'
    )
    button2 = InlineKeyboardButton(
        text='No',
        callback_data='no'
    )
    update.message.reply_text(
        text='Desea eliminar su cuenta?\nEsta accion no se puede deshacer',
        reply_markup=InlineKeyboardMarkup([
            [button1],[button2]
        ])
        )
    
    
    ##funciones------------------------
    def borrarpj(update,context):

        print('BorrarAUTH: '+str(AUTH))
        userid = update.callback_query.from_user['id']
        useridsect = '%s' %userid
        INI.read('C:/Users/Eli/Documents/GitHub/DonJuezCidBot/botcid/users/users.ini')

        if INI.has_section(useridsect) and (userid == AUTH):
            INI.remove_section(useridsect)
            with open('C:/Users/Eli/Documents/GitHub/DonJuezCidBot/botcid/users/users.ini','w') as userini:
                INI.write(userini)
                userini.close()
                query = update.callback_query
                query.answer
                query.edit_message_text(
                    text='Usted ha sido eliminado del sistema')
                return 0
        elif userid == AUTH:
            with open('C:/Users/Eli/Documents/GitHub/DonJuezCidBot/botcid/users/users.ini') as  userini:
                userini.close()
                query = update.callback_query
                query.answer
                query.edit_message_text(
                    text='Usted no esta registrado en el sistema ')
                return 0
        else:
            return 0


    def noborrarpj(update,context):

        userid = update.callback_query.from_user['id']

        if userid == AUTH:
        
            query = update.callback_query
            query.answer
            query.edit_message_text(
                text='Cancelado')
            return 0

#    def test(update,context):
#        query = update.callback_query
#        query.answer
#
#        query.edit_message_text(
#             text='testeado correctamente'
#        )
    
##handlers------------------------------------------
    dp.add_handler(CallbackQueryHandler(pattern='si',callback=borrarpj))
    dp.add_handler(CallbackQueryHandler(pattern='no',callback=noborrarpj))
    return 0



 
class deletepj(object):

    def __init__(self):
        return

    def __repr__(self):
        return 'test'

    def __str__(self):
        return 'test2'

    def start(self,update, context,INI,dp,ID,DICT,GET,INLKB,INLKM,CBCKQH):
        AUTH = GET
        print('StartAUTH: '+str(AUTH))

        button1 = INLKB(
            text='Si',
            callback_data='si'
        )
        button2 = INLKB(
            text='No',
            callback_data='no'
        )
        update.message.reply_text(
            text='Desea eliminar su cuenta?\nEsta accion no se puede deshacer',
            reply_markup=INLKM([
                [button1],[button2]
            ])
            )
        print('StartAUTH2: '+str(AUTH))
    
    ##funciones------------------------
        def borrarpj(update,context):
            print('BorrarAUTH: '+str(AUTH))
            print('BorrarGET: '+str(GET))
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
                    DICT.delkey(ID)
                    return 0
            elif userid == AUTH:
                with open('C:/Users/Eli/Documents/GitHub/DonJuezCidBot/botcid/users/users.ini') as  userini:
                    userini.close()
                    query = update.callback_query
                    query.answer
                    query.edit_message_text(
                        text='Usted no esta registrado en el sistema ')
                    DICT.delkey(ID)
                    return 0
            else:
                pass


        def noborrarpj(update,context):
            print('NoBorrarAUTH: '+str(AUTH))

            userid = update.callback_query.from_user['id']

            if userid == AUTH:
        
                query = update.callback_query
                query.answer
                query.edit_message_text(
                    text='Cancelado')
                DICT.delkey(ID)
                return 0

#    def test(update,context):
#        query = update.callback_query
#        query.answer
#
#        query.edit_message_text(
#             text='testeado correctamente'
#        )
    
##handlers------------------------------------------
        dp.add_handler(CBCKQH(pattern='si',callback=borrarpj))
        dp.add_handler(CBCKQH(pattern='no',callback=noborrarpj))

    
##-----------randonw---------------------
def start(update,context,INI,ID,DICT):
    userid = ID
    useridsect = '%s' %userid
    INI.read('C:/Users/Eli/Documents/GitHub/DonJuezCidBot/botcid/users/users.ini')

    if INI.has_section(useridsect):
        with open('C:/Users/Eli/Documents/GitHub/DonJuezCidBot/botcid/users/users.ini') as userini:
            userini.close()
            update.message.reply_text('Usted ya ha sido registrado, por favor haga buen uso del sistema: '+str(useridsect))
            DICT.delkey(ID)
                
    else:
        INI.add_section(useridsect)
        with open('C:/Users/Eli/Documents/GitHub/DonJuezCidBot/botcid/users/users.ini', 'w') as  userini:
            INI.write(userini)
            userini.close()

            update.message.reply_text('Su ID ha sido registrado, por favor elija un apodo para continuar')
            DICT.delkey(ID)
#-----------funciones------------------------------------

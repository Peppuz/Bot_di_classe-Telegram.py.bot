##########################################################################

# Divertentismo

def Pomes(b , u):
    if u.message.text in ('Pomes' , 'pomes'):
        b.sendMessage(chat_id=u.message.chat_id, text="Pomes? Muta!")

def tette(bot, up):
    if ('tette', 'Tette') in up.message.text:
        bot.sendPicture()

def Sierda(b , u):
    if u.message.text in ('Sierda', 'sierda'):
        b.sendMessage(u.message.chat_id, text="Sierda curnutu!")
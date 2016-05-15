##########################################################################

# Prenotazione alla Lista

def addFisica(bot, update):
    addF(update.message.text[16:])
    bot.sendMessage(chat_id=update.message.chat_id, text="Sei" +update.message.text[16:]+ '. Ti ho aggiunto alla /listafisica', reply_markup=hidekb)
def addF(x):
    lettura = open('5C/Fisica.txt')
    lista_lettura = [i.rstrip() for i in lettura.readlines(0)]
    ricomposizione_in_String = '\n'.join(map(str,lista_lettura))
    aggiunta = ricomposizione_in_String + '\n' + ''.join(map(str,x))
    lettura.close()
    scrittura = open('5C/Fisica.txt', 'w').write(aggiunta)
    lettura.close()

def addMate(bot, update):
    addM(update.message.text[15:])
    bot.sendMessage(chat_id=update.message.chat_id, text="Sei " + update.message.text[15:] + '. Ti ho aggiunto alla /listamate', reply_markup=hidekb)
def addM(x):
    lettura = open('5C/Mate.txt')
    lista_lettura = [i.rstrip() for i in lettura.readlines(0)]
    ricomposizione_in_String = '\n'.join(map(str,lista_lettura))
    aggiunta = ricomposizione_in_String + '\n' + ''.join(map(str,x))
    lettura.close()
    scrittura = open('5C/Mate.txt', 'w').write(aggiunta)
    lettura.close()

def addArte(bot, update):
    addA(update.message.text[15:])
    bot.sendMessage(chat_id=update.message.chat_id, text="Sei " +update.message.text[15:]+ '. Ti ho aggiunto alla /listaarte', reply_markup=hidekb)
def addA(x):
    lettura = open('5C/Arte.txt')
    lista_lettura = [i.rstrip() for i in lettura.readlines(0)]
    ricomposizione_in_String = '\n'.join(map(str,lista_lettura))
    aggiunta = ricomposizione_in_String + '\n' + ''.join(map(str,x))
    lettura.close()
    scrittura = open('5C/Arte.txt', 'w').write(aggiunta)
    lettura.close()

def addLatino(bot, update):
    addL(update.message.text[17:])
    bot.sendMessage(chat_id=update.message.chat_id, text="Sei " +update.message.text[17:]+ '. Ti ho aggiunto alla /listaLatino', reply_markup=hidekb)
def addL(x):
    lettura = open('5C/Latino.txt')
    lista_lettura = [i.rstrip() for i in lettura.readlines(0)]
    ricomposizione_in_String = '\n'.join(map(str,lista_lettura))
    aggiunta = ricomposizione_in_String + '\n' + ''.join(map(str,x))
    lettura.close()
    scrittura = open('5C/Latino.txt', 'w').write(aggiunta)
    lettura.close()


print 'Check .prenotazioni'

##########################################################################

##########################################################################

# Base Commands

def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id,
                    text='Buonasera! Per ora non so fare un cazzo, ma mi stanno programmando...', reply_markup=hidekb)
def stop(bot, update):
    if update.message.from_user.id ==135605474:
        bot.sendMessage(chat_id=update.message.chat_id, text="BOT OFFLINE! "+ telegram.Emoji.FACE_WITHOUT_MOUTH, reply_markup=hidekb)
        updater.stop()
    else:
        bot.sendMessage(chat_id=update.message.chat_id, text="Non hai accesso al comando")
def sconosciuto(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text='Basta scia!', reply_markup=hidekb)
def kb(bot,update):
    bot.sendMessage(chat_id=update.message.chat_id, text='ok.', reply_markup=hidekb)
def novita(bot, update):
    if "Novita'" in update.message.text:
        KK = telegram.ReplyKeyboardMarkup([['Nascondi la Tastiera']])
        bot.sendMessage(chat_id=update.message.chat_id, text="Le novita di oggi: 1. /prenotamiMateria \n es. /prenotamiFisica Peppuz \r\n 2. /listaLatino \r\n 3. /mancantiInLatino", reply_markup=KK)

print 'Loading --> .base'

##########################################################################
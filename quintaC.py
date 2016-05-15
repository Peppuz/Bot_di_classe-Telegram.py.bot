##########################################################################
# Settings
# -*- coding: utf-8 -*-
import telegram
from telegram.ext import Updater ,filters, CommandHandler, MessageHandler
import datetime 
import urllib
import urllib2
from bs4 import BeautifulSoup
import time
##########################################################################


# Setup
bot = telegram.Bot(token='183806893:AAECOcmBqcSEK8IiYwsU2gXFiXc7nP1EvmE')
updater = Updater(token='183806893:AAECOcmBqcSEK8IiYwsU2gXFiXc7nP1EvmE')
hidekb = telegram.ReplyKeyboardHide()
Oggi = datetime.datetime.today().weekday()

##########################################################################

# Base Commands

def start(bot, update):
    bot.sendMessage(update.message.chat_id, text="Se hai bisogno basta premere sul comando \n --> /aiuto")
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
        bot.sendMessage(chat_id=update.message.chat_id, text="Ricerca diretta: \n /w WolframAlpha")
def comandi(bot, update):
    comandikb = [["Novita'"],['/oggi','/domani', '/liste'],['/elenco', 'Nascondi la Tastiera']]
    reply = telegram.ReplyKeyboardMarkup(comandikb)
    bot.sendMessage(chat_id=update.message.chat_id,
                    text="Tutti i comandi sono li, nella tastiera, basta premerne uno", reply_markup=reply)
def kbh(bot, update):
    if 'Nascondi la Tastiera' in update.message.text:
        bot.sendMessage(chat_id=update.message.chat_id, text='Tastiera Nascosta', reply_markup=hidekb)
##########################################################################

# Materie & Elenco

def oggi(bot, update):
    if Oggi == 0:
        bot.sendMessage(chat_id=update.message.chat_id, text="Oggi e' Lunedi: \r\n Filosofia \r\n Ed. Fisica \r\n Matematica \r\n Storia \r\n Scienze", reply_markup=hidekb)
    if Oggi == 1:
        bot.sendMessage(chat_id=update.message.chat_id, text="Oggi e' Martedi: \r\n Filosofia \r\n Fisica \r\n Matematica \r\n Storia \r\n Scienze", reply_markup=hidekb)
    if Oggi == 2:
        bot.sendMessage(chat_id=update.message.chat_id,text="Oggi e' Mercoledi: \r\n Scienze \r\n Italiano \r\n Religione \r\n Latino \r\n Matematica", reply_markup=hidekb)
    if Oggi == 3:
        bot.sendMessage(chat_id=update.message.chat_id,text="Oggi e' Giovedi: \r\n Arte \r\n Ed. Fisica \r\n Fisica \r\n Filosofia \r\n Inglese", reply_markup=hidekb)
    if Oggi == 4:
        bot.sendMessage(chat_id=update.message.chat_id,text="Oggi e' Venerdi: \r\n Inglese \r\n Matematica \r\n Scienze \r\n Italiano \r\n Italiano", reply_markup=hidekb)
    if Oggi == 5:
        bot.sendMessage(chat_id=update.message.chat_id,text="Oggi e' Sabatooooooo: \r\n Storia \r\n Latino \r\n Latino \r\n Arte \r\n Inglese", reply_markup=hidekb)
    if Oggi == 6:
        bot.sendMessage(chat_id=update.message.chat_id,text="Oggi e' Domenica, coglione, al massimo chiedimi cosa abbiamo /domani", reply_markup=hidekb)
def domani(bot, update):
    if Oggi == 6:
        fil = open('5C/Orari.txt').read()
        bot.sendMessage(update.message.chat_id, text=fil[0:100], reply_markup=hidekb)
def dopodomani(bot, update):
    if Oggi == 5:
        bot.sendMessage(chat_id=update.message.chat_id, text="Dopodomani e' Lunedi: \r\n Filosofia \r\n Ed. Fisica \r\n Matematica \r\n Storia \r\n Scienze", reply_markup=hidekb)
    if Oggi == 6:
        bot.sendMessage(chat_id=update.message.chat_id, text="Dopodomani e' Martedi: \r\n Filosofia \r\n Fisica \r\n Matematica \r\n Storia \r\n Scienze", reply_markup=hidekb)
    if Oggi == 0:
        bot.sendMessage(chat_id=update.message.chat_id,text="Dopodomani e' Mercoledi: \r\n Scienze \r\n Italiano \r\n Religione \r\n Latino \r\n Matematica", reply_markup=hidekb)
    if Oggi == 1:
        bot.sendMessage(chat_id=update.message.chat_id,text="Dopodomani e' Giovedi: \r\n Arte \r\n Ed. Fisica \r\n Fisica \r\n Filosofia \r\n Inglese", reply_markup=hidekb)
    if Oggi == 2:
        bot.sendMessage(chat_id=update.message.chat_id,text="Dopodomani e' Venerdi: \r\n Inglese \r\n Matematica \r\n Scienze \r\n Italiano \r\n Italiano", reply_markup=hidekb)
    if Oggi == 3:
        bot.sendMessage(chat_id=update.message.chat_id,text="Dopodomani e' Sabatooooooo: \r\n Storia \r\n Latino \r\n Latino \r\n Arte \r\n Inglese", reply_markup=hidekb)
    if Oggi == 4:
        bot.sendMessage(chat_id=update.message.chat_id, text="Dopodoma e' Domenica  " + telegram.Emoji.KISSING_FACE_WITH_SMILING_EYES, reply_markup=hidekb)
def elenco(bot, update):
    gg = open('5C/elenco.txt', 'r')
    bot.sendMessage(chat_id=update.message.chat_id, text=gg.read(), reply_markup=hidekb)

##########################################################################

# Prenotazione alla Lista

def addFisica(bot, update, args):
    addF(args)
    bot.sendMessage(chat_id=update.message.chat_id, text="Ok, " +args+ '. Ti ho aggiunto alla /listaFisica', reply_markup=hidekb)
def addF(x):
    lettura = open('5C/Fisica.txt')
    lista_lettura = [i.rstrip() for i in lettura.readlines(0)]
    ricomposizione_in_String = '\n'.join(map(str,lista_lettura))
    aggiunta = ricomposizione_in_String + '\n' + ''.join(map(str,x))
    lettura.close()
    scrittura = open('5C/Fisica.txt', 'w').write(aggiunta)
    lettura.close()
def addMate(bot, update, args):
    addM(args)
    bot.sendMessage(chat_id=update.message.chat_id, text="Sei " + args + '. Ti ho aggiunto alla /listaMate', reply_markup=hidekb)
def addM(x):
    lettura = open('5C/Mate.txt')
    lista_lettura = [i.rstrip() for i in lettura.readlines(0)]
    ricomposizione_in_String = '\n'.join(map(str,lista_lettura))
    aggiunta = ricomposizione_in_String + '\n' + ''.join(map(str,x))
    lettura.close()
    scrittura = open('5C/Mate.txt', 'w').write(aggiunta)
    lettura.close()
def addArte(bot, update,args):
    addA(update.message.text[15:])
    bot.sendMessage(chat_id=update.message.chat_id, text="Sei " +args+ '. Ti ho aggiunto alla /listaArte', reply_markup=hidekb)
def addA(x):
    lettura = open('5C/Arte.txt')
    lista_lettura = [i.rstrip() for i in lettura.readlines(0)]
    ricomposizione_in_String = '\n'.join(map(str,lista_lettura))
    aggiunta = ricomposizione_in_String + '\n' + ''.join(map(str,x))
    lettura.close()
    scrittura = open('5C/Arte.txt', 'w').write(aggiunta)
    lettura.close()
def addLatino(bot, update,args):
    addL(args)
    bot.sendMessage(chat_id=update.message.chat_id, text="Sei " +args+ '. Ti ho aggiunto alla /listaLatino', reply_markup=hidekb)
def addL(x):
    lettura = open('5C/Latino.txt')
    lista_lettura = [i.rstrip() for i in lettura.readlines(0)]
    ricomposizione_in_String = '\n'.join(map(str,lista_lettura))
    aggiunta = ricomposizione_in_String + '\n' + ''.join(map(str,x))
    lettura.close()
    scrittura = open('5C/Latino.txt', 'w').write(aggiunta)
    lettura.close()

print 'Loading --> .prenotazioni'	

##########################################################################

# Liste

def listemain(bot,update):
    tastieraListe = [['/lScienze','/lFisica'],['/lMate','/lArte']]
    kb = telegram.ReplyKeyboardMarkup(tastieraListe)
    bot.sendMessage(chat_id=update.message.chat_id, text='Seleziona la lista: ', reply_markup=kb)
    
def listaFisica(bot, update):
    file = open('5C/Fisica.txt')
    linee = file.read()
    bot.sendMessage(chat_id=update.message.chat_id, text=linee, reply_markup=hidekb)
    file.close()
    
def listaMate(bot, update):
    file = open('5C/Mate.txt')
    linee = file.read()
    bot.sendMessage(chat_id=update.message.chat_id, text=linee, reply_markup=hidekb)
    file.close()
    
def listaArte(bot, update):
    file = open('5C/Arte.txt')
    linee = file.read()
    bot.sendMessage(chat_id=update.message.chat_id, text=linee, reply_markup=hidekb)
    file.close()
    
def listaLatino(bot,update):
    ita = open('5C/Latino.txt')
    linee = ita.read()
    bot.sendMessage(chat_id=update.message.chat_id, text=linee, reply_markup=hidekb)
    ita.close()
    
def mancantiLatino(bot, update):   #Lista di chi manca
    ff = open('5C/Mancanti-Latino.txt', 'r')
    text = ff.read()
    bot.sendMessage(chat_id=update.message.chat_id, text=text, reply_markup=hidekb)
    ff.close()
    
def Scienze(b,u):
    gg = open('5C/Scienze.txt').read()
    b.sendMessage(u.message.chat_id, text=gg, reply_markup=hidekb)
    
def Storia(b,u):
    gg = open('5C/Storia.txt')
    b.sendMessage(u.message.chat_id, text=gg.read(), reply_markup=hidekb)

print "Check .liste"

#########################################################################

# Area Riservata alla prof

mycode = 135605474
DPcode = 176559360
interrogaStoria = 0

def prof(b, u):
    profC=telegram.ReplyKeyboardMarkup(profcommands)
    profcommands= [['Devo interrogare in Storia!'], ['/listaStoria']]
    if (mycode , DPcode) in u.message.from_user.id:
        b.sendMessage(u.message.chat_id, text='Logged as Prof.', reply_markup=profC)
    if u.message.from_user.id not in (DPcode, umycode):
        b.sendMessage(u.message.chat_id, 'Mi spiace non sei autorizzato.', reply_markup=hidekb)
	
def devointerrogare(b,u):
    if u.message.text in ("Devo interrogare in Storia!", 'Interrogo storia'):
        if u.message.from_user.id in (mycode, DPcode):
            interrogaStoria = 1
            b.sendMessage(u.message.chat_id, 'Chi ha bisogno di interrogare prof?', reply_markup=hidekb)
	
def chiinterroga(b,u):
    if u.message.from_user.id in (mycode, DPcode):
        if interroga == 1:
            x = u.message.text
            lettura = open('5C/Storia.txt')
            lista_lettura = [i.rstrip() for i in lettura.readlines(0)]
            ricomposizione_in_String = '\n'.join(map(str,lista_lettura))
            aggiunta = ricomposizione_in_String + '\n' + ''.join(map(str,x))
            lettura.close()
            scrittura = open('5C/Storia.txt', 'w').write(aggiunta)
            lettura.close()
            b.sendMessage(u.message.chat_id, 'Bene! Ho aggiunto '+ x + ' alla lista. \n /listaStoria per controllare', reply_markup=hidekb)
            interroga = 0
  
print 'Loading --> .prof'
		
#########################################################################

# Area Fun
def Pomes(b , u):
    if u.message.text in ('Pomes', 'pomes'):
        b.sendMessage(chat_id=u.message.chat_id, text="Pomeeeeees!")
def Sierda(b , u):
    if u.message.text in ('Sierda', 'sierda'):
        b.sendMessage(u.message.chat_id, text="Sierda curnutu!")
def cristo(bot, up):
    if ('cristo','Cristo') in up.message.text:
        bot.sendMessage(chat_id=up.message.chat_id, text="Porco Dio, non bestemmiare. Pezzente!", reply_markup=hidekb)
#########################################################################

# Dev Area

def dev(bot, up):
    if up.message.from_user.id == mycode:
        k = [['/adm-stop'],['/adm-kb'],[telegram.Emoji.AIRPLANE]]
        devKB = telegram.ReplyKeyboardMarkup(k)
        bot.sendMessage(chat_id=up.message.chat_id, text="Comandi disponibili per i Testers: ", reply_markup=devKB)
    else:
        bot.sendMessage(up.message.chat_id, "Non hai accesso all'area!")
def listening_admin(b,u):
    if 'TT' in u.message.text:
        b.sendMessage(chat_id=u.message.from_user.id, text="Troia")
def myID(b,u):
    b.sendMessage(chat_id=u.message.chat_id, text=u.message.from_user.id + " ")
print 'Loading --> .fun'

##########################################################################

# WolframAlpha
def wf(b,u):
    s = u.message.text[3:]
    params = urllib.urlencode({'i':s})
    pagehttp = 'http://m.wolframalpha.com/input/?'+params
    b.sendMessage(u.message.chat_id, text=pagehttp)
    strin = urllib2.urlopen(pagehttp)
    b.sendMessage(chat_id=u.message.chat_id, text="Attendi, sto elaborando le risposte... \n ~8sec")
    time.sleep(8)
    string_html = strin.read()
    bs = BeautifulSoup(string_html, "html.parser")
    divs = bs.body.find_all(class_='output pnt', limit=5)
    imgs = BeautifulSoup(str(divs), "html.parser").find_all('img')
    get_from =  "\n".join(set(tag['src'] for tag in imgs))
    links = get_from.strip().split('\n')
    for value in links:
        b.sendPhoto(u.message.chat_id, photo=value)
print "################"
##########################################################################

# Main

def main():
	
    disp = updater.dispatcher
		
# Testing
    disp.addHandler(CommandHandler("w",wf))
    disp.addHandler(CommandHandler('dev', dev))
    disp.addHandler(MessageHandler([filters.TEXT],listening_admin))
    disp.addHandler(CommandHandler('id',myID))
	
# Prof
    disp.addHandler(CommandHandler('prof', prof))
    disp.addHandler(CommandHandler('listaStoria', Storia))
    disp.addHandler(MessageHandler([filters.TEXT],[filters.TEXT],chiinterroga))
    disp.addHandler(MessageHandler([filters.TEXT],devointerrogare))

# Base
    disp.addHandler(CommandHandler('start', start))
    disp.addHandler(CommandHandler('adm-stop', stop))
    disp.addHandler(CommandHandler('aiuto', comandi))
    disp.addHandler(CommandHandler('adm-kb', kb))
    disp.addHandler(MessageHandler([filters.TEXT],kbh))
    #disp.addUnknownTelegramCommandHandler(sconosciuto)

# Liste
    disp.addHandler(CommandHandler('liste',listemain))
    disp.addHandler(CommandHandler('lFisica', listaFisica))
    disp.addHandler(CommandHandler('lMate', listaMate))
    disp.addHandler(CommandHandler('lArte', listaArte))
    disp.addHandler(CommandHandler('lLatino', listaLatino))
    disp.addHandler(CommandHandler('lScienze', Scienze))


# Prenotazioni
    disp.addHandler(CommandHandler('prenotamiFisica', addFisica))
    disp.addHandler(CommandHandler('prenotamiMate', addMate))
    disp.addHandler(CommandHandler('prenotamiArte', addArte))
    disp.addHandler(CommandHandler('prenotamiLatino', addLatino))

# Materie
    disp.addHandler(CommandHandler('elenco', elenco))
    disp.addHandler(CommandHandler('oggi', oggi))
    disp.addHandler(CommandHandler('domani', domani))
    disp.addHandler(CommandHandler('dopodomani', dopodomani))

# Fun
    disp.addHandler(MessageHandler([filters.TEXT],Sierda))
    disp.addHandler(MessageHandler([filters.TEXT],Pomes))
    disp.addHandler(MessageHandler([filters.TEXT],cristo))

    updater.start_polling()

if __name__ == '__main__':
    main()
    print 'Ready!'

##########################################################################

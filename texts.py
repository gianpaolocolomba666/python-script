from telegram.ext import *
from telegram import *
#from emoji import emojize

#comandi con bottoni tastiera
infoSpedizioni = "\U0001f4e6 Ships"
listaGusti = "\U0001f924 Lista Gusti" 
prezzoPuff = "\U0001f4b8 Prezzo Puffs"
recensioni = "\U0001f4dd Ch Recensioni"
immagini = "\U0001f5bc\ufe0f Immagini"
contatti = "\u260e\ufe0f Contatti"
informazioni = "\u2139\ufe0f Info Puffs"

#risposte a comandi
answer_prezzoPuff = "Listino Prezzi dei nostri prodotti: \n\
 - 1 Vape 15€ + Spedizione \n\
 - 5 Vape 85€ + Spedizione Free\n\
 - 10 Vape 125€ + Spedizione Free \n\
 - 20 Vape 215€ + Spedizione Free \n\
 - 50 Vape 440€ + Spedizione Free \n\n\
 Per maggiori quantità contattaci in privato!👇"

answer_infoSpedizioni = "\U0001f4e6 Contattaci in privato per ricevere una spedizione su misura per te!\n\n\
Spedizioni in 24/48h 🚛"

answer_recensioni = "📝 A questo link puoi raggiungere il canale recensioni! \n\n\
t.me/UnclePuffRecensioni"

answer_immagini = "In allegato le immagini dei nostri prodotti:" 

answer_contatti = "\u26a0\ufe0f Attenzione alla @!!! \u26a0\ufe0f\n\n\
Per ordinare e chiedere informazioni contattaci direttamente qui sotto! \U0001f447"

answer_informazioni = "Vape Bang:\n\
  • 5000 Tiri 🌬️\n\
  • Batteria Ricaricabile 🔋\n\
  • 5% di nicotina 🚬\n\n\
Vape Elfbar:\n\
  • 5000 Tiri 🌬️ \n\
  • Batteria Ricaricabile 🔋\n\
  • 5% di nicotina 🚬\n\n\
Per ordinare contattaci qui sotto 😉"

#messaggio di benvenuto
welcome_message = 'Benvenuto nel bot ufficiale di\n\
            🇮🇹 @unclepufff 💨\n\n\
Con questo bot potrai:\n\n \
• Avere le informazioni necessarie prima di acquistare.\n \
• Vedere tu stesso le recensioni dei nostri clienti.\n \
• Ricevere assistenza da parte del nostro Team.\n\n \
🤖 Utilizza i pulsanti qui sotto per navigare nello shop 💨'

token_bot = "5443605402:AAHm5uWp7Jq2voir7wuv-RyTsBxfB0b7CW8"

#pulsanti link contatti
keyboard_contatti = [[InlineKeyboardButton("KRIM", url="t.me/fuckkgod"), InlineKeyboardButton("SLENDERMAN", url="t.me/Slenderman22"), InlineKeyboardButton("CARAXES", url="t.me/caraxes0")]]

#immagini
pic1 = 'photo\pic1.jpg'
pic2 = 'photo\pic2.jpg'
pic3 = 'photo\pic3.jpg'

/*from emoji import emojize*/
from telegram import *
from telegram.ext import *

import texts

updater = Updater(texts.token_bot, use_context=True)
dispatcher = updater.dispatcher


def start(update: Update, context: CallbackContext):
    chat_id= update.message.chat_id
    print(update.message.message_id)
    custom_keyboard = [[texts.informazioni, texts.prezzoPuff],
                      [texts.listaGusti, texts.recensioni],
                      [texts.immagini, texts.contatti, texts.infoSpedizioni]]
    context.bot.send_message(chat_id=chat_id, text=texts.welcome_message, reply_markup=ReplyKeyboardMarkup(custom_keyboard, resize_keyboard=True))
    
def messageHandler(update: Update, context: CallbackContext):
    chat_id= update.message.chat_id
    if texts.listaGusti in update.message.text:
        context.bot.forward_message(chat_id= chat_id, from_chat_id='-1001624799334', message_id='203')
    if texts.prezzoPuff in update.message.text:
        context.bot.send_message(chat_id=chat_id, text=texts.answer_prezzoPuff)
    if texts.infoSpedizioni in update.message.text:
        context.bot.send_message(chat_id=chat_id, text=texts.answer_infoSpedizioni)
    if texts.recensioni in update.message.text:
        context.bot.send_message(chat_id=chat_id, text=texts.answer_recensioni)
    if texts.immagini in update.message.text:
        context.bot.send_message(chat_id=chat_id, text=texts.answer_immagini)
        context.bot.send_photo(chat_id=chat_id, photo= open(texts.pic1, 'rb'))
        context.bot.send_photo(chat_id=chat_id, photo= open(texts.pic2, 'rb'))
        context.bot.send_photo(chat_id=chat_id, photo= open(texts.pic3, 'rb'))
    if texts.contatti in update.message.text:
        context.bot.send_message(chat_id=chat_id, reply_markup= InlineKeyboardMarkup(texts.keyboard_contatti, resize_keyboard=True), text = texts.answer_contatti)
    if texts.informazioni in update.message.text:
        context.bot.send_message(chat_id=chat_id, text=texts.answer_informazioni)
        

dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(MessageHandler(Filters.text, messageHandler))

updater.start_polling()

from telegram.ext import Updater, CommandHandler, MessageHandler
from telegram.ext.filters import Filters
import response as r
import requests
import json
import time
from constant import telegram_api


print("TG_BOT is online")
def start(update, context):
    t= time.strftime("%H,%M,%S")
    if(t > "0,0,0" and t < "11,59,59"):
        greet = "good morning"
    elif(t >"12,0,0" and t < "17,59,59"):
        greet = "good afternoon"    
    elif(t > "17,0,0" and t < "23,59,59"):
        greet = "good evening"
    context.bot.send_message(chat_id=update.effective_chat.id, text= greet+", I'm TG_BOT")

# def gamecmd(update, context):
#     text = str(update.message.text).lower()
#     context.bot.send_message(chat_id=update.effective_chat.id, text='im Kurama')
#     context.bot.send_message(chat_id=update.effective_chat.id,text= "let play")
#     if text == "yes":
#         update.message.reply_text("sure")

def handle_message(update,context):
    text = str(update.message.text).lower()
    if text.startswith('game'):
        response = r.game(text)
    else:    
        response = r.sample_response(text)
    update.message.reply_text(response)

def main():
    updater = Updater(telegram_api , use_context=True)
    dispatcher = updater.dispatcher
    start_handler = CommandHandler('start', start)
    reply_handler = MessageHandler(Filters.text & (~Filters.command), handle_message)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(reply_handler)
    updater.start_polling()

if __name__ == '__main__':
    main()




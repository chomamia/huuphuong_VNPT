
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

updater = Updater("5547536251:AAGq1De6wC2j_nzjILFYBE-LhslrwNYpRXo",
                  use_context=True)
  

def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Chao xìn! Mình là em Bot dễ thương của anh Phương nè :v")

def help(update: Update, context: CallbackContext):
    update.message.reply_text("Your Message")
def gmail_url(update: Update, context: CallbackContext):
    update.message.reply_text("huuphuongtp@gmail.com")
  
  
def youtube_url(update: Update, context: CallbackContext):
    update.message.reply_text("https://www.youtube.com/watch?v=ugMi2cbXC_U")
  
def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry I can't recognize you , you said '%s'" % update.message.text)
  
  
def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry '%s' is not a valid command" % update.message.text)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('youtube', youtube_url))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('gmail', gmail_url))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(
    Filters.command, unknown))  # Filters out unknown commands
  
# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))
  
updater.start_polling()
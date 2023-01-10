from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters, ConversationHandler
from random import randint
import functions

app = ApplicationBuilder().token('5883434456:AAE_hP3ksro3k54qU1I794bo1brDN2u9MuQ').build()

app.add_handler(ConversationHandler(entry_points= [CommandHandler('game', functions.game)], 
                                    states={functions.my_turn:[MessageHandler(filters.TEXT, functions.gamer_turn)], 
                                           functions.bot:[MessageHandler(filters.TEXT, functions.bot_turn)]},
                                    fallbacks=[CommandHandler('cancel', functions.cancel)]))

app.add_handler(CommandHandler('hello', functions.hello))
app.add_handler(MessageHandler(filters.TEXT, functions.del_word))


app.run_polling()
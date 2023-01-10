from telegram import Bot
from telegram.ext import Updater

# TOKEN = 5883434456:AAE_hP3ksro3k54qU1I794bo1brDN2u9MuQ

bot = Bot(token='5883434456:AAE_hP3ksro3k54qU1I794bo1brDN2u9MuQ')
updater = Updater(token='5883434456:AAE_hP3ksro3k54qU1I794bo1brDN2u9MuQ')
dispatcher = updater.dispatcher
updater.start_polling()


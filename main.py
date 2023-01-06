from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


app = ApplicationBuilder().token("5883434456:AAE_hP3ksro3k54qU1I794bo1brDN2u9MuQ").build()

app.add_handler(CommandHandler("hello", hello))

app.run_polling()
import logging
import os

from flask import Flask
from dotenv import load_dotenv
from telegram import BotCommand, Update
from telegram.ext import Application, ContextTypes, MessageHandler, filters

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.WARNING
)

# Set Flask application
app = Flask(__name__)



@app.route("/", methods=["GET", "POST"])
async def webhook():
    update = Update
    print(update)
    await update.message.reply_text(update.message.text) 



async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text
    await update.message.reply_text(text)


load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
PORT = int(os.getenv("PORT")) # type: ignore
application = Application.builder().token(BOT_TOKEN).updater(None).build()
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
# application.run_polling()
application.run_webhook(
    listen='0.0.0.0',
    port=PORT,
    secret_token=BOT_TOKEN.split(':')[1],
    webhook_url='https://PDA.pythonanywhere.com:8443'
)


if __name__ == "__main__":
    app.run()
from flask import Flask
from threading import Thread
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import os
import asyncio

TOKEN = os.getenv("7609587534:AAFcO_DqL5G9yVO7JkthVDcOYZqjCE-LHxY")
app = Flask(__name__)

# Just to keep Render Web Service active
@app.route("/")
def home():
    return "Castro-bot is running."

# Telegram bot handlers
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Castro-bot is online and listening 🤖")

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text.lower()
    if "who made you" in msg:
        await update.message.reply_text("👑 I was created by the one and only Castro.")
    else:
        await update.message.reply_text("Always listening in the shadows...")

async def run_bot():
    application = Application.builder().token("7609587534:AAFcO_DqL5G9yVO7JkthVDcOYZqjCE-LHxY").build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))

    await application.initialize()
    await application.start()
    await application.updater.start_polling()

def start_bot():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(run_bot())

# Start bot in a separate thread
Thread(target=start_bot).start()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))

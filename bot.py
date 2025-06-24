from flask import Flask
from threading import Thread
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import os
import asyncio

app = Flask(__name__)
TOKEN = os.getenv("7609587534:AAFcO_DqL5G9yVO7JkthVDcOYZqjCE-LHxY")

# Bot logic
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hey! Castro-bot is here, loud and clear! 🔥")

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text.lower()
    if "who made you" in msg:
        await update.message.reply_text("👑 I was created by Castro, ruler of this code.")
    else:
        await update.message.reply_text("Just chilling in the Render cloud ☁️")

async def run_bot():
    print("🔥 Starting Telegram bot polling loop...")
    application = Application.builder().token("7609587534:AAFcO_DqL5G9yVO7JkthVDcOYZqjCE-LHxY").build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))
    await application.initialize()
    await application.start()
    await application.updater.start_polling()
    print("✅ Polling loop is live!")

def start_bot():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(run_bot())

@app.route("/")
def home():
    return "Castro-bot Flask server is up."

# Start the polling thread when Flask starts
Thread(target=start_bot).start()

if __name__ == "__main__":
    print("🚀 Launching Flask app...")
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))

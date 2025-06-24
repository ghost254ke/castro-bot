from flask import Flask
from threading import Thread
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import os
import asyncio

app = Flask(__name__)
TOKEN = os.getenv("7609587534:AAFcO_DqL5G9yVO7JkthVDcOYZqjCE-LHxY")

# Route for Render to detect the web service
@app.route("/")
def home():
    return "🟢 Castro-bot is running."

# Telegram bot commands
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hey! I'm Castro-bot and I'm running on Render 😎")

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    if "who made you" in text:
        await update.message.reply_text("I was built by the legendary Castro 👑")
    else:
        await update.message.reply_text("Still here, still listening 🔊")

# Polling loop
async def run_bot():
    print("🎯 Starting polling loop...")
    app_telegram = Application.builder().token("7609587534:AAFcO_DqL5G9yVO7JkthVDcOYZqjCE-LHxY").build()
    app_telegram.add_handler(CommandHandler("start", start))
    app_telegram.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))
    await app_telegram.initialize()
    await app_telegram.start()
    await app_telegram.updater.start_polling()
    print("✅ Telegram bot polling is live!")

# Background thread for polling
def start_polling_thread():
    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(run_bot())
    except Exception as e:
        print(f"❌ Polling crashed: {e}")

# Start bot on launch
Thread(target=start_polling_thread).start()

if __name__ == "__main__":
    print("🚀 Launching Flask server...")
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))

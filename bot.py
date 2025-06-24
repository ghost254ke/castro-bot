from flask import Flask
from threading import Thread
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import os
import asyncio

app = Flask(__name__)
TOKEN = os.getenv("7609587534:AAFcO_DqL5G9yVO7JkthVDcOYZqjCE-LHxY")

@app.route("/")
def home():
    return "🟢 Castro-bot is running on Render."

# Telegram bot handlers
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Yo! Castro-bot is online, smooth as always 🕶️")

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text.lower()
    if "who made you" in msg:
        await update.message.reply_text("I was handcrafted by Castro the legend 👑")
    else:
        await update.message.reply_text("I'm running in the Render cloud, always watching 👀")

# Run the Telegram bot in a separate thread
async def run_bot():
    print("🔥 Launching Telegram polling...")
    bot_app = Application.builder().token("7609587534:AAFcO_DqL5G9yVO7JkthVDcOYZqjCE-LHxY").build()
    bot_app.add_handler(CommandHandler("start", start))
    bot_app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))
    await bot_app.initialize()
    await bot_app.start()
    await bot_app.updater.start_polling()
    print("✅ Polling loop started")

def start_polling_thread():
    try:
        print("🌀 Starting polling thread...")
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(run_bot())
    except Exception as e:
        print(f"❌ Polling crashed: {e}")

Thread(target=start_polling_thread).start()

if __name__ == "__main__":
    print("🚀 Starting Flask app...")
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))

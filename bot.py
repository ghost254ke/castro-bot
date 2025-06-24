from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os
import asyncio

BOT_TOKEN = os.getenv("7609587534:AAFcO_DqL5G9yVO7JkthVDcOYZqjCE-LHxY")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hey! I'm a Telegram bot built by Castro 🤖")

async def main():
    app = Application.builder().token("7609587534:AAFcO_DqL5G9yVO7JkthVDcOYZqjCE-LHxY").build()
    app.add_handler(CommandHandler("start", start))

    print("✅ Castro-bot is online!")
    await app.initialize()
    await app.start()
    await app.updater.start_polling()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except RuntimeError:
        loop = asyncio.get_event_loop()
        loop.create_task(main())
        loop.run_forever()

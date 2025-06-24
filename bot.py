from flask import Flask, request
import telegram
import os

TOKEN = os.getenv("7609587534:AAFcO_DqL5G9yVO7JkthVDcOYZqjCE-LHxY")
bot = telegram.Bot(token="7609587534:AAFcO_DqL5G9yVO7JkthVDcOYZqjCE-LHxY")

app = Flask(__"castro-bot"__)

@app.route('/')
def home():
    return "Castro-bot is alive!"

@app.route(f'/{"7609587534:AAFcO_DqL5G9yVO7JkthVDcOYZqjCE-LHxY"}', methods=['POST'])
def respond():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    text = update.message.text.lower()

    if text == "/start":
        bot.sendMessage(chat_id=chat_id, text="Hey! I'm Castro's bot 🤖 Ready to chat.")
    elif "who made you" in text or "your creator" in text:
        bot.sendMessage(chat_id=chat_id, text="My creator is the brilliant Castro 👑")
    else:
        bot.sendMessage(chat_id=chat_id, text="I'm listening...")

    return 'ok'

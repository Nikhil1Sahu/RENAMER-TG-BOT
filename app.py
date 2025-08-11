from flask import Flask
from threading import Thread
import os
from pyrogram import Client

# ------------------ Flask App ------------------
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!", 200

def run_flask():
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

# ------------------ Start Bot ------------------
def start_bot():
    # Create your bot client (make sure config.py has the API_ID, API_HASH, BOT_TOKEN)
    bot = Client(
        "my_bot",
        api_id=int(os.environ.get("API_ID")),
        api_hash=os.environ.get("API_HASH"),
        bot_token=os.environ.get("BOT_TOKEN")
    )

    bot.run()

# ------------------ Main ------------------
if __name__ == "__main__":
    Thread(target=run_flask).start()  # Start Flask in separate thread
    start_bot()                       # Start bot in main thread

from flask import Flask, request
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Replace with your actual bot token
TOKEN = '7205713684:AAEFtrxxIjHvMEBg-Vd3fki_YgopbJfVcU0'

# Flask web server initialization
app = Flask(__name__)

# Bot initialization
updater = Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Define your handlers here
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Hello! I'm your bot.")

# Command handler
dispatcher.add_handler(CommandHandler("start", start))

# Function to reply "Hello" when the bot starts
def hello() -> None:
    print("Bot started! Saying hello...")
    # Replace with your desired message
    updater.bot.send_message(chat_id='@YOUR_CHANNEL_ID', text='Hello!')

# Register handler to run when bot starts
updater.start_polling()
hello()

# Flask route to set up webhook
@app.route(f'/{TOKEN}', methods=['POST'])
def webhook() -> str:
    """Webhook endpoint for Telegram updates."""
    update = Update.de_json(request.get_json(force=True), updater.bot)
    dispatcher.process_update(update)
    return 'ok'

if __name__ == '__main__':
    # Start Flask server
    app.run(port=8443)
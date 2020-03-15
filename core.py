from flask import Flask, request, jsonify

from telegram_bot import TelegramBot
from config import TELEGRAM_INIT_WEBHOOK_URL
from sql import Sql

import logging

# Init logging
logging.basicConfig(level = logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

app = Flask(__name__)

print(TELEGRAM_INIT_WEBHOOK_URL)

TelegramBot.init_webhook(TELEGRAM_INIT_WEBHOOK_URL)

# Initiallize SQL here
db = Sql()

@app.route('/webhook', methods=['POST'])
def index():

    req = request.get_json()

    # Use the same instance of db
    bot = TelegramBot(db)

    # Parse the user message
    bot.parse_webhook_data(req)

    # Get the result 
    success = bot.action(req)

    return jsonify(success=success) # TODO: Success should reflect the success of the reply

if __name__ == '__main__':

    print("Initiallizing the database")

    db.createTables()

    app.run(port=8080)

def printShit():
    print("shit")

# https://telegram.me

# check bot initialization: https://api.telegram.org/bot<822448732:AAGUNRBnPPHjVhOqySQZk_QzP_VaZhgx9i0>/getme
# check webhook url: https://api.telegram.org/bot822448732:AAGUNRBnPPHjVhOqySQZk_QzP_VaZhgx9i0/getWebhookInfo
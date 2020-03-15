import requests
import json

from config import TELEGRAM_SEND_MESSAGE_URL

TYPE_CAPTION = 0
TYPE_PHOTO = 1
TYPE_TEXT = 2

def print_formatted(request):

        print("*****************************")
        print(json.dumps(request, sort_keys= True, indent= 4))
        print("*****************************")

class TelegramBot:

    def __init__(self, db):
        self.db = db

    def parse_webhook_data(self, data):
        """
        Parses Telegram JSON request from webhook and sets fields for conditional actions
        Args:
            data:str: JSON string of data
        """

        print_formatted(data)
    
        keys = data["message"].keys()

        print(keys)

        if ("caption" in keys):
            print("Contains photo with caption")   
            self.type = TYPE_CAPTION
        elif ("photo" in keys):
            print("Contains photo")
            self.type = TYPE_PHOTO
        elif ("text" in keys):
            print("Contains text") 
            self.type = TYPE_TEXT

        message = data['message']

        if message['text'] == "/start":
            self.db.insertUser(message)

        self.chat_id = message['chat']['id']
        self.first_name = message['from']['first_name']      

    def action(self, req):
        """
        Conditional actions based on set webhook data.
        Returns:
            bool: True if the action was completed successfully else false
        """

        success = None

        message = req["message"]

        if self.type == TYPE_CAPTION:
          
            print("Processing Caption")

            print_formatted(message["caption"])
            print_formatted(message["photo"])

        elif self.type == TYPE_PHOTO:

            print("Processing Photo")

            print_formatted(message["photo"])
        else:     

            print("Processing Text")
            print_formatted(message["text"])
            
        success = self.send_message()

        return success

    def send_message(self):
        """
        Sends message to Telegram servers.
        """

        # TODO Save the sent message

        res = requests.get(TELEGRAM_SEND_MESSAGE_URL.format(self.chat_id, "Kir"))

        return True if res.status_code == 200 else False
    
    @staticmethod
    def init_webhook(url):
        """
        Initializes the webhook
        Args:
            url:str: Provides the telegram server with a endpoint for webhook data
        """

        requests.get(url)

    @staticmethod
    def get_webhook(url):

        # Getinfo about webhook

        return requests.get(url)

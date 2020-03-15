import requests

TOKEN = "1129627099:AAHQm_8egX4-tY7s49goyuiexVqw6Q2krac"

NGROK_URL = "https://3991433a.ngrok.io"
BASE_TELEGRAM_URL = f"https://api.telegram.org/bot{TOKEN}"
LOCAL_WEBHOOK_ENDPOINT = f"{NGROK_URL}/webhook"  

TELEGRAM_INIT_WEBHOOK_URL = BASE_TELEGRAM_URL + f"/setWebhook?url={LOCAL_WEBHOOK_ENDPOINT}"
TELEGRAM_SEND_MESSAGE_URL = BASE_TELEGRAM_URL + "/sendMessage?chat_id={}&text={}"

# WebHook https://api.telegram.org/bot1129627099:AAHQm_8egX4-tY7s49goyuiexVqw6Q2krac/setWebhook?url=https://ff9152d1.ngrok.io/webhook

# Webhook https://api.telegram.org/bot1129627099:AAHQm_8egX4-tY7s49goyuiexVqw6Q2krac/setWebhook?url=https  ://ff9152d1.ngrok.io/webhook

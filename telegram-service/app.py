from flask import Flask
from threading import Thread
import os
import time
import random
from utils.telegram_client import TelegramService

app = Flask(__name__)
service = None

@app.route('/')
def health_check():
    return "Notification Service Operational", 200

def start_service():
    global service
    service = TelegramService(
        os.getenv('TG_API_ID'),
        os.getenv('TG_API_HASH'),
        os.getenv('TG_SESSION_STR')
    )
    service.run()

if __name__ == "__main__":
    Thread(target=start_service).start()
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 3000)))

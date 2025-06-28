
import requests

def send_telegram_alert(message, bot_token, chat_id):
    try:
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        data = {"chat_id": chat_id, "text": message}
        response = requests.post(url, data=data)
        response.raise_for_status()
    except Exception as e:
        print(f"Telegram alert failed: {e}")

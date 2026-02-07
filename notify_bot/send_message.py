import json
import os
import sys
import requests
import configparser

USERS_FILE = os.path.join(os.path.expanduser("~"), ".notify-bot", "users.json")
CONFIG_FILE = os.path.join(os.path.expanduser("~"), ".notify-bot", "config.ini")


def get_token():
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE, encoding="utf-8")
    return config["DEFAULT"]["Token"]


def get_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    return []


def send_message(user_id, message):
    try:
        token = get_token()
    except Exception:
        print("Отсутствует токен. Установите токен командой set-token.")
        return None

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": user_id,
        "text": message,
    }

    try:
        response = requests.post(url, json=payload, timeout=10)
        if response.status_code != 200:
            print(f"Ошибка отправки сообщения к {user_id}: {response.text}")
    except Exception as e:
        print(f"Ошибка отправки сообщения к {user_id}: {e}")


def main():
    if len(sys.argv) < 2:
        print("Использование: send-message \"текст рассылки\"")
        return

    message = " ".join(sys.argv[1:])
    users = get_users()
    if not users:
        print("Список пользователей пуст. Сначала нажмите /start в боте с нужного аккаунта.")
        return

    for user_id in users:
        send_message(user_id, message)


if __name__ == "__main__":
    main()
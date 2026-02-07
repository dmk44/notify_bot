import os
import configparser
import requests

CONFIG_FILE = os.path.join(os.path.expanduser('~'), '.notify-bot', 'config.ini')

os.makedirs(os.path.dirname(CONFIG_FILE), exist_ok=True)


def get_bot_username(token: str) -> str | None:
    """
    Пытаемся получить имя бота через Telegram API.
    Если не удалось (неверный токен / нет сети и т.п.) — возвращаем None.
    """
    url = f"https://api.telegram.org/bot{token}/getMe"
    try:
        resp = requests.get(url, timeout=5)
        data = resp.json()
        if data.get("ok") and "result" in data and "username" in data["result"]:
            return data["result"]["username"]
    except Exception:
        # Нам важно не упасть при установке токена
        return None
    return None


def set_token():
    token = input("Введите токен вашего Телеграм-бота: ")

    bot_username = get_bot_username(token)

    config = configparser.ConfigParser()
    config["DEFAULT"] = {"Token": token}
    if bot_username:
        config["DEFAULT"]["BotUsername"] = bot_username

    with open(CONFIG_FILE, "w", encoding="utf-8") as configfile:
        config.write(configfile)

    if bot_username:
        print(f"Токен для бота @{bot_username} установлен.")
    else:
        print("Токен установлен (не удалось автоматически определить имя бота).")


def main():
    set_token()


if __name__ == "__main__":
    main()
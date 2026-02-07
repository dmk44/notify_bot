import json
import os
import sys
import configparser

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

USERS_LIST = os.path.join(os.path.expanduser("~"), ".notify-bot", "users.json")
CONFIG_FILE = os.path.join(os.path.expanduser("~"), ".notify-bot", "config.ini")


def get_token():
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE, encoding="utf-8")
    try:
        return config["DEFAULT"]["Token"]
    except Exception:
        print("Токен не установлен. Установите токен командой set-token.")
        raise SystemExit(1)


def get_bot_username() -> str | None:
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE, encoding="utf-8")
    return config["DEFAULT"].get("BotUsername")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    add_user(user_id)

    bot_username = get_bot_username()

    text_lines = ["Привет от Notify-bot ;-)."]
    text_lines.append("Вы добавлены в список рассылки этого бота.")
    if bot_username:
        text_lines.append(f"Бот: @{bot_username}")

    await update.message.reply_text("\n".join(text_lines))


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(update.message.text)


def add_user(user_id):
    if os.path.exists(USERS_LIST):
        with open(USERS_LIST, "r", encoding="utf-8") as file:
            users = json.load(file)
    else:
        users = []

    if user_id not in users:
        users.append(user_id)
        os.makedirs(os.path.dirname(USERS_LIST), exist_ok=True)
        with open(USERS_LIST, "w", encoding="utf-8") as file:
            json.dump(users, file, ensure_ascii=False)


def get_users():
    if os.path.exists(USERS_LIST):
        with open(USERS_LIST, "r", encoding="utf-8") as file:
            return json.load(file)
    return []


async def send_message_to_all(context: ContextTypes.DEFAULT_TYPE, message: str):
    users = get_users()
    for user_id in users:
        try:
            await context.bot.send_message(chat_id=user_id, text=message)
        except Exception as e:
            print(f"Ошибка отправки сообщения к {user_id}: {e}")


def main():
    token = get_token()
    application = ApplicationBuilder().token(token).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    application.run_polling()


if __name__ == "__main__":
    main()
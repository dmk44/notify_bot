import os

CONFIG_FILE = os.path.join(os.path.expanduser("~"), ".notify-bot", "config.ini")


def clear_token():
    if os.path.exists(CONFIG_FILE):
        os.remove(CONFIG_FILE)
        dir_path = os.path.dirname(CONFIG_FILE)
        try:
            if not os.listdir(dir_path):
                os.rmdir(dir_path)
        except Exception:
            pass
        print("Токен удалён.")
    else:
        print("Токен не найден.")


def main():
    clear_token()


if __name__ == "__main__":
    main()
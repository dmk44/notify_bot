import os

USERS_FILE = os.path.join(os.path.expanduser("~"), ".notify-bot", "users.json")


def clear_users():
    if os.path.exists(USERS_FILE):
        os.remove(USERS_FILE)
        dir_path = os.path.dirname(USERS_FILE)
        try:
            if not os.listdir(dir_path):
                os.rmdir(dir_path)
        except Exception:
            pass
        print("Список пользователей очищен.")
    else:
        print("Список пользователей не найден.")


def main():
    clear_users()


if __name__ == "__main__":
    main()
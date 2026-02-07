# notify-bot

**English** | [Русский](README.ru.md)

A simple Python CLI for sending messages through your Telegram bot.

**What does it do?** 

*notify-bot* turns your bot into a pager:  
the operator works from Bash / PowerShell, and users receive notifications in Telegram.

## Requirements
- Python **3.9+**

## Installation
From the project root:
```bash
git clone ...
pip install .
```

On Windows this is usually enough. 
On Linux and macOS you may need to install inside a virtual environment or use `pipx`.

After installation, the following console commands are available:

- `set-token` — Set the bot token and save it to the config;
- `start-bot` — Start the bot (collects users into a mailing list);
- `send-message` — Send a message to all saved users in the list;
- `clear-users` — Clear the user list;
- `clear-token` — Remove the token.

## Setup
1. Get a token from [@BotFather](https://t.me/BotFather).
2. Run:

```bash
set-token
```

You enter the token and the script will:

- Save the token to `~/.notify-bot/config.ini`;
- Try to auto-detect the bot username via the Telegram API;
- Print something like: `Token for bot @bot_name has been set.`

## Usage
1. Register users:

```bash
start-bot
```

While the command is running, users should press `/start` in your bot.

Each user will:

* be added to `users.json`;
* receive a confirmation message.

> Hello from notify-bot ;-)
> You have been added to the mailing list.
> Bot: @bot_name

**Note:**
The bot does not need to run permanently.
Once users are registered, the process can be stopped at any time.
Users are stored locally in: `~/.notify-bot/users.json`

2. Send a broadcast

```bash
send-message "Your message text"
```
The message will be delivered to all saved users.

## Security
A Telegram bot token gives full control over the bot, so treat it like a password.

By default, notify-bot stores the token locally.
Encrypting the token without a separate secret usually does not provide meaningful security benefits.

### Linux / macOS
You may restrict access to the directory and files:
```bash
chmod 700 ~/.notify-bot
chmod 600 ~/.notify-bot/config.ini
chmod 600 ~/.notify-bot/users.json
```

This prevents other users on the system from reading the token or mailing list.

### Windows
The standard user profile security model is used.
No additional actions are typically required.

## Cleanup and removal
- `clear-users` — Removes `~/.notify-bot/users.json` (the user list);
- `clear-token` — Removes `~/.notify-bot/config.ini` and, if needed, the `~/.notify-bot` directory;
- `pip uninstall notify-bot` — Uninstalls the package from Python.
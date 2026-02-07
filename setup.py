from setuptools import setup, find_packages

setup(
    name='notify-bot',
    version='1.3',
    packages=find_packages(),
    install_requires=[
        'python-telegram-bot>=20.0',
        'requests',
        'cryptography',
    ],
    entry_points={
        'console_scripts': [
            'start-bot=notify_bot.start_bot:main',
            'send-message=notify_bot.send_message:main',
            'clear-users=notify_bot.clear_users:main',
            'clear-token=notify_bot.clear_token:main',
            'set-token=notify_bot.set_token:main',
        ],
    },
)

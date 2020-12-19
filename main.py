import os,telebot

import requests

# pyTelegramBotAPI boto

is_prod = os.environ.get('IS_HEROKU', None)

bot_token = os.environ.get('TELEGRAM_TOKEN', None)

print(bot_token)


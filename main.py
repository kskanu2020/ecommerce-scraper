import os

import requests,telebot

# pyTelegramBotAPI boto

is_prod = os.environ.get('IS_HEROKU', None)

bot_token = os.environ.get('TELEGRAM TOKEN', "")

print(bot_token)

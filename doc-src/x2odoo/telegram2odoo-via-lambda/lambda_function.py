import telegram  # https://github.com/python-telegram-bot/python-telegram-bot
import sys
import os
import logging
import re
import json


logger = logging.getLogger()
LOG_LEVEL = os.environ.get('LOG_LEVEL')
if LOG_LEVEL:
    logger.setLevel(getattr(logging, LOG_LEVEL))


BOT_TOKEN = os.environ.get('BOT_TOKEN')
TELEGRAM_USER_ID = int(os.environ.get('TELEGRAM_USER_ID'))


RESPONSE_200 = {
    "statusCode": 200,
    "headers": {},
    "body": ""
}



def lambda_handler(event, context):
    logger.debug("Event: \n%s", event)

    bot = telegram.Bot(token=BOT_TOKEN)
    update_json = json.loads(event["body"])
    update = telegram.Update.de_json(update_json, bot)

    chat = message.chat
    user = message.from_user
    text = message.text

    if user.id != TELEGRAM_USER_ID:
        bot.sendMessage(chat_id=chat.id, text="This is a private bot, sorry. If you want similary bot, check documentation at website https://odoo-sync.sh")
         return RESPONSE_200

    odoo = TODO

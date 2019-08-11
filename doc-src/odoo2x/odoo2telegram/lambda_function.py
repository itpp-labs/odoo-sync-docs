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
TELEGRAM_USER_ID = os.environ.get('TELEGRAM_USER_ID')


def lambda_handler(event, context):
    logger.debug("Event: \n%s", event)
    data = json.loads(event['body'])

    bot = telegram.Bot(token=BOT_TOKEN)
    message = "New task is created by %s:\n%s" % (data['created_by_name'], data['task_name'])
    bot.sendMessage(TELEGRAM_USER_ID, message)

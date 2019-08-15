import telegram  # https://github.com/python-telegram-bot/python-telegram-bot
import sys
import os
import logging
import re
import json
 import urllib.parse as urlparse


logger = logging.getLogger()
LOG_LEVEL = os.environ.get('LOG_LEVEL')
if LOG_LEVEL:
    logger.setLevel(getattr(logging, LOG_LEVEL))


BOT_TOKEN = os.environ.get('BOT_TOKEN')
TELEGRAM_USER_ID = int(os.environ.get('TELEGRAM_USER_ID'))
OPENAPI_SPECIFICATION_URL = int(os.environ.get('OPENAPI_SPECIFICATION_URL'))
ODOO_DATABASE_NAME = int(os.environ.get('ODOO_DATABASE_NAME'))
ODOO_USER_TOKEN = int(os.environ.get('ODOO_USER_TOKEN'))


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

     odoo_address = urlparse.urlparse(OPENAPI_SPECIFICATION_URL)
     host = odoo_address.hostname
     http_client = RequestsClient()
     http_client.set_basic_auth(
         host, ODOO_DATABASE_NAME, ODOO_USER_TOKEN 
     )
     odoo = SwaggerClient.from_url(
         OPENAPI_SPECIFICATION_URL,
         http_client=http_client,
     )

     res = odoo.note_note.addNoteNote(body={'memo': text})
     note_id = TODO
     note_url = ''.join(OPENAPI_SPECIFICATION_URL.split('/')[:3])
     note_url = '%s/web?id=%s&view_type=form&model=note.note' % (note_url, note_id)
     bot.sendMessage(chat_id=chat.id, text="Note is created: %s" % note_url, reply_to_message_id=message.message_id)
     return RESPONSE_200

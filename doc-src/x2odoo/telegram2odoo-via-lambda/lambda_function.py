import os
import logging
import json
import urllib.parse as urlparse

# https://github.com/python-telegram-bot/python-telegram-bot
import telegram
# https://github.com/Yelp/bravado
from bravado.requests_client import RequestsClient
from bravado.client import SwaggerClient


logger = logging.getLogger()
LOGGING_LEVEL = os.environ.get('LOGGING_LEVEL')
if LOGGING_LEVEL:
    logger.setLevel(getattr(logging, LOGGING_LEVEL))


BOT_TOKEN = os.environ.get('BOT_TOKEN')
TELEGRAM_USER_ID = int(os.environ.get('TELEGRAM_USER_ID'))
ODOO_OPENAPI_SPECIFICATION_URL = os.environ.get('ODOO_OPENAPI_SPECIFICATION_URL')
ODOO_OPENAPI_TOKEN = os.environ.get('ODOO_OPENAPI_TOKEN')


RESPONSE_200 = {
    "statusCode": 200,
    "headers": {},
    "body": ""
}



def lambda_handler(event, context):
    logger.debug("Event: \n%s", json.dumps(event))

    bot = telegram.Bot(token=BOT_TOKEN)
    update_json = json.loads(event["body"])
    update = telegram.Update.de_json(update_json, bot)
    message = update.message

    chat = message.chat
    user = message.from_user
    text = message.text

    if user.id != TELEGRAM_USER_ID:
        bot.sendMessage(chat_id=chat.id, text="This is a private bot, sorry. If you want similary bot, check documentation at website https://odoo-sync.sh")
        return RESPONSE_200

    openapi_url = urlparse.urlparse(ODOO_OPENAPI_SPECIFICATION_URL)
    host = openapi_url.hostname
    db = urlparse.parse_qs(openapi_url.query)['db'][0]

    http_client = RequestsClient()
    http_client.set_basic_auth(
        host, db, ODOO_OPENAPI_TOKEN
    )
    odoo = SwaggerClient.from_url(
        ODOO_OPENAPI_SPECIFICATION_URL,
        http_client=http_client,
    )

    res = odoo.note_note.addNoteNote(body={'memo': text}).response().result
    note_id = res['id']
    note_url = '/'.join(ODOO_OPENAPI_SPECIFICATION_URL.split('/')[:3])
    note_url = '%s/web#id=%s&view_type=form&model=note.note' % (note_url, note_id)
    bot.sendMessage(chat_id=chat.id, text="Note is created: %s" % note_url, reply_to_message_id=message.message_id)
    return RESPONSE_200

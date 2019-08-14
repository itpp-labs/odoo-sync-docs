=========================================================
 Create Notes in Odoo from messages sent to Telegram bot
=========================================================

Here we'll make a telegram bot, that receives your message and create a Note in Odoo with the same content. You'll need:

* .. include:: ../../templates/you_need_telegram_to_create_bot.rst
* .. include:: ../../templates/you_need_aws_to_create_lambda.rst
* .. include:: ../../templates/you_need_odoo_openapi.rst

.. contents::
   :local:


Deployment
==========

Create a bot
------------

.. include:: ../../templates/create_telegram_bot.rst

Prepare zip file
----------------

.. include:: ../../templates/make_lambda_zip.rst

::

    mkdir /tmp/bot
    cd /tmp/bot

    pip3 install python-telegram-bot -t .
    wget https://raw.githubusercontent.com/it-projects-llc/odoo-sync/master/doc-src/x2odoo/telegram2odoo-via-lambda/lambda_function.py
    zip -r /tmp/bot.zip *

Create Lambda function
----------------------

Runtime
~~~~~~~

Use ``Python 3.6``

Function code
~~~~~~~~~~~~~

.. include:: ../../templates/upload_lambda_zip.rst

Environment variables
~~~~~~~~~~~~~~~~~~~~~

* .. include:: ../../templates/lambda_env_bot_token.rst
* .. include:: ../../templates/lambda_env_logging_level.rst
* .. include:: ../../templates/lambda_env_telegram_user_id.rst

Trigger
~~~~~~~
.. include:: ../../templates/lambda_trigger.rst

Register telegram webhook
-------------------------

Tell telegram to send notifications to lambda function when bot receives new messages

.. code-block:: sh

    BOT_TOKEN="PASTE_BOT_TOKEN_HERE"
    INVOKE_URL="https://PASTE-YOUR-INVOKE-URL"
    curl -XPOST https://api.telegram.org/bot${BOT_TOKEN}/setWebhook --data-urlencode="url=${INVOKE_URL}"

Try it out
==========

* In telegram: send a message to the bot
* In Odoo: open menu ``[[ Notes ]]``
* RESULT: new note is created
* .. include:: ../../templates/check_odoo_cloudwatch_logs.rst

Source
======

Key script of the bot is presented below:

.. literalinclude:: lambda_function.py
   :language: python

.. include:: ../../templates/contactus.rst

=======================================
 Telegram notification on Odoo Updates
=======================================

Here we'll make a telegram bot, that sends you notification whenever new task
assigned to you is created. You'll need:

* .. include:: ../../templates/you_need_telegram_to_create_bot.rst
* .. include:: ../../templates/you_need_aws_to_create_lambda.rst
* .. include:: ../../templates/you_need_odoo_webhook.rst


.. contents::
   :local:

Deployment
==========

Create a bot
------------
.. include:: ../../templates/create_telegram_bot.rst

Prepare zip file
----------------
.. include ../../templates/make_lambda_zip.rst

::

    mkdir /tmp/bot
    cd /tmp/bot

    pip3 install python-telegram-bot -t .
    wget https://raw.githubusercontent.com/it-projects-llc/odoo-sync/master/doc-src/odoo2x/odoo2telegram/lambda_function.py
    zip -r /tmp/bot.zip *


Create Lambda function
----------------------

.. include:: ../../templates/create_lambda.rst

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

Register lambda webhook
-----------------------
.. include:: ../../templates/base_automation_webhook-create-rule.rst
..

  * **Model:** *Task* (``project.task``)
  * **Trigger Condition**: *On Creation*
  * Filter by task by users:

    * In Odoo 10.0: set **Filter** to ``[["user_id","=",123]]``
    * In Odoo 11.0+: set **Apply On** to ``[["user_id","=",123]]``
    
    Here ``123`` is your user ID. To get the ID, navigate to ``[[ Settings ]] >> Users`` menu, open your user, check ID value in the browser URL

  * **Python Code**:

    .. code-block:: py

       INVOKE_URL="https://PASTE-YOUR-INVOKE-URL"
       data = {
           "task_name": record.name,
           "created_by_name": record.create_uid.name,
       }
       log("Sending to webhook: %s" % data)
       requests.post(INVOKE_URL, json=data)

Try it out
==========

* Open created telegram bot and send any message to it. It's needed to allow bot send a message to you.
* Open Odoo and create new task assigned to you.
* RESULT: the bot will send you a notification
* .. include:: ../../templates/check_odoo_cloudwatch_logs.rst

Source
======

Key script of the bot is presented below:

.. literalinclude:: lambda_function.py
   :language: python

.. include:: ../../templates/contactus.rst


 

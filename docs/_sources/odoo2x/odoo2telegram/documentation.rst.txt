=======================================
 Telegram notification on Odoo Updates
=======================================

Here we'll make a telegram bot, that sends you notification whenever new task
assigned to you is created. You need:

* `Telegram <https://telegram.org/>`__ account to receive messages
* AWS Account to use `AWS Lambda <https://aws.amazon.com/lambda/>`__
* `Odoo <https://www.odoo.com/>`__  with admin access to setup `Webhooks <https://apps.odoo.com/apps/modules/10.0/base_automation_webhook/>`__

.. contents::
   :local:

Deployment
==========

Create a bot
------------
https://telegram.me/botfather -- follow instruction to set bot name and get bot token.

Check your steps:

* Use the /newbot command to create a new bot first.
* The name of the bot must be end witn "bot" (e.g. TetrisBot or tetris_bot).
* Keep your token secure and store safely, it can be used by anyone to control your bot.

Prepare zip file
----------------
To make `deployment package <https://docs.aws.amazon.com/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html>`__ execute following commands::

    mkdir /tmp/bot
    cd /tmp/bot

    pip3 install python-telegram-bot -t .
    wget https://raw.githubusercontent.com/it-projects-llc/odoo-sync/master/doc-src/odoo2x/odoo2telegram/lambda_function.py
    zip -r /tmp/bot.zip *


Create Lambda function
----------------------

Runtime
~~~~~~~

Use ``Python 3.6``

Function code
~~~~~~~~~~~~~
* Set **Code entry type** to *Upload a .zip file*
* Select ``bot.zip`` file you made

Environment variables
~~~~~~~~~~~~~~~~~~~~~
* ``BOT_TOKEN`` -- the one you got from BotFather
* ``TELEGRAM_USER_ID`` -- put here your ID. You can get one by sending any message to `Get My ID bot <https://telegram.me/itpp_myid_bot>`__
* ``LOGGING_LEVEL`` -- Level of loger. (Allowed values: DEBUG, INFO, CRITICAL, ERROR, WARNING), by default: INFO

Trigger
~~~~~~~
* **API Gateway**. Once you configure it and save, you will see ``Invoke URL`` under Api Gateway **details** section
* Set the security mechanism for your API endpoint as *Open*

Register webhook
----------------
* Open Odoo
* Install module `Outgoing Webhooks Module <https://apps.odoo.com/apps/modules/10.0/base_automation_webhook/>`__
* Create an Automated Action with the following values (see `Module Documentation <https://apps.odoo.com/apps/modules/10.0/base_automation_webhook/>`__ for details):

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
* If something goes wrong, check Odoo logs and `CloudWatch <https://aws.amazon.com/cloudwatch/>`__ logs

Source
======

Key script of the bot is presented below:

.. literalinclude:: lambda_function.py
   :language: python

.. include:: ../../contactus.rst


 

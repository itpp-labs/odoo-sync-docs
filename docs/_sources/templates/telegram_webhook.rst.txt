Tell telegram to send notifications to lambda function when bot receives new messages

.. code-block:: sh

    # set your values
    BOT_TOKEN="PASTE_BOT_TOKEN_HERE"
    INVOKE_URL="https://PASTE-YOUR-INVOKE-URL"

    # execute command below without changes
    curl -XPOST https://api.telegram.org/bot${BOT_TOKEN}/setWebhook --data-urlencode "url=${INVOKE_URL}"

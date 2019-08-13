=======================================================================
 Send PUSH notification when an eCommerce product becomes out of stock
=======================================================================

You'll need:

* .. include:: ../../templates/you_need_odoo_webhook.rst
* .. include:: ../../templates/you_need_ifttt.rst
* A mobile phone with `Android <https://play.google.com/store/apps/details?id=com.ifttt.ifttt&hl=en>`__ or `iOS <https://apps.apple.com/us/app/ifttt/id660944635>`__ app installed.

Prepare IFTTT Webhook URL
=========================

* Open Webhook page at IFTTT: https://ifttt.com/maker_webhooks
* Click Documentation
* Choose some event name, e.g. ``product-out-of-stock``
* Copy the url. It has following format: ``https://maker.ifttt.com/trigger/EVENT_NAME/with/key/SOME-KEY``

Register Webhook
================

.. include:: ../../templates/base_automation_webhook-create-rule.rst
..

  * **Model:** Stock Move (``stock.move``)
  * **Trigger Condition**: *On Update*
  * **Before Update Domain**: ``[['state', '!=', 'done'], ['product_id.website_published', '=', True]]``

    * Note, that in Odoo 10.0 field is called **Filter**
    
  * **Apply on**: ``[['state', '=', 'done'],['product_id.website_published', '=', True],["product_id.qty_available","<=",0]]``

    * Note, that in Odoo 10.0 field is located in *Server Action* model and called **Condition**

  * **Python Code**:

    .. code-block:: py

       INVOKE_URL="https://PASTE-IFTTT-WEBHOOK-URL"
       base_url = env['ir.config_parameter'].get_param('web.base.url');
       template_id = record.product_id.product_tmpl_id.id
       image_url = base_url + "/website/image/product.template/%s/image/90x90" % template_id
       product_url = base_url + "/shop/product/%s" % template_id
       data = {
           "value1": record.product_id.name,
           "value2": image_url,
           "value3": product_url,
       }
       log("Sending to webhook: %s" % data)
       requests.post(INVOKE_URL, json=data)


.. We cannot add condition ["product_id.qty_available", ">", 0] to Before Update Domain
.. From my understanding, it's because qty is changed slighly before updating stock.move and even before updating stock.move.line
.. For most cases we don't really need for that check



Prepare IFTTT applet
====================

* Open url: https://ifttt.com/create
* **This**: search and select *Webhooks*

  * Choose *Receive a web request*
  * Set **Event Name** (in our example, ``product-out-of-stock``)

* **That**: search and select *Notifications*

  * Chose *Send a reach notification from the IFTTT app*

    * **Message**: ``Product {{Value1}} is out of stock!``
    * **Link URL**: ``{{Value3}}``
    * **Image URL**: ``{{Value2}}``

Try it out
==========

Be sure, that:

* *eCommerce* and *Inventory Management* modules are installed in Odoo
* There is at least one product, which is:

  * *Stockable Product*
  * Published on Website
  * Is not out of stock yet

Now,

* make module out of stock (e.g. make a fake order at website or just make Inventory Adjustment).
* RESULT: you can see PUSH notification on your phone

.. TODO IMAGE

* .. include:: ../../templates/check_odoo_or_ifttt_logs.rst

.. include:: ../../templates/contactus.rst

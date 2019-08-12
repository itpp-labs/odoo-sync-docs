=======================================================================
 Send PUSH notification when an eCommerce product becomes out of stock
=======================================================================

You'll need:

* .. include:: ../../templates/you_need_odoo_webhook.rst
* .. include:: ../../templates/you_need_ifttt.rst
* A mobile phone with `Android <https://play.google.com/store/apps/details?id=com.ifttt.ifttt&hl=en>`__ or `iOS <https://apps.apple.com/us/app/ifttt/id660944635>`__ app installed.

Register webhook
================

.. include:: ../../templates/base_automation_webhook-create-rule.rst
..

  * **Model:** *Packing Operation* (``stock.move.line``)
  * **Trigger Condition**: *On Creation & Update*
  * **Before Update Domain**: ``[["product_id.qty_available",">",0]]``

    * Note, that in Odoo 10.0 field is called **Filter**
    
  * **Apply on**: ``[["product_id.qty_available","<=",0]]``

    * Note, that in Odoo 10.0 field is located in *Server Action* model and called **Condition**

  * **Python Code**:

    .. code-block:: py

       INVOKE_URL="https://PASTE-IFTTT-WEBHOOK-URL"
       data = {
           "value1": record.product_id.name,
           "value2": TODO,
           "value3": TODO,
       }
       log("Sending to webhook: %s" % data)
       requests.post(INVOKE_URL, json=data)


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

TODO IMAGE

* .. include:: ../../templates/check_odoo_or_ifttt_logs.rst

.. include:: ../../templates/contactus.rst

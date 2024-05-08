===============
Sale Order Delivery Address Updater
===============

Description
-----------

This Odoo module enhances the functionality of the sale order quotation form by adding a button that opens a wizard. This wizard allows users to select a delivery address associated with the customer of the sale order. Upon selection, the delivery address in the sale order is automatically updated with the chosen address, streamlining the process of managing delivery details.

Features
--------

- Adds a button to the sale order quotation form to open a wizard.
- Wizard contains a Many2one field listing delivery addresses of the selected customer.
- Enables users to update the delivery address of the sale order by selecting from available addresses in the wizard.
- Automatically updates the sale order's delivery address upon selection in the wizard, ensuring accurate delivery information.

Installation
------------

1. Download the module ZIP file from https://github.com/AnandShah10/change_delivery_address.git.
2. Extract the contents of the ZIP file.
3. Place the extracted folder in the `addons` directory of your Odoo installation.
4. Restart the Odoo server.
5. Update the list of modules in Odoo to include the new module.
6. Search for "Sale Order Delivery Address Updater" in the Apps menu and install it.
7. Once installed, the functionality will be available in the sale order quotation form.

Usage
-----

1. Navigate to the Sales module in Odoo.
2. Create or open a sale order quotation.
3. Locate the new button labeled "Update Delivery Address" on the quotation form.
4. Click the "Update Delivery Address" button to open the wizard.
5. In the wizard, select the desired delivery address from the Many2one field.
6. After selecting the delivery address, click the "Update" or "Confirm" button.
7. The sale order's delivery address will be automatically updated with the selected address.
8. Save the sale order to apply the changes.

Compatibility
-------------

- This module is compatible with Odoo version 17.0.

Credits
-------

- Anand Shah - Developer

License
-------

GPL-3

Support
-------

For any questions, issues, or feedback regarding this module, please contact:
- shahanand1072004@gmail.com

Disclaimer
----------

This module is provided as-is, without any warranty, expressed or implied. Use at your own risk.

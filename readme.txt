"http://127.0.0.1:8000/item_list/" = Displaying all available items and deleting a specific item

"http://127.0.0.1:8000/add_item/" = Adding a new item

"http://127.0.0.1:8000/edit_item/" = Updating the details of a specific item

item_list.html = Now lists the items taken from the items database

add_item.html = Now sends item name and price to the backend to be added as a new item

edit_item.html = Now edits an item entry based on its pk

views.py = Views are now able to send and receive data from the user and manipulate the database

models.py = Added the new models, namely item, order, item_order 



edit_item.html and add_item.html = added entry for stock_quantity

models.py = Added stock_quantity attribute to item model

views.py = Edited edit_item and add_item views to accept stock_quantity,
            Added confirm order view

openpos.html = Made the form submit data to django and edited table to list items.
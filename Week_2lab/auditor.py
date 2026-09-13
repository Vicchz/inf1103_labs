'''Initialize Inventory to 0

run a loop asking enter stock quantity untill type quit

accept stock as integer

handle invalid input etc ten

reject nagtive number

keep inventory updated 

if inventory > 500, alert and break loop

when type quit, print total unit processed and numbe failed rejected entries'''

inventory = 0

while True:
    Entry = input("Enter stock quantity:")

    if str(Entry) == "quit":
        break

    quantity = int(Entry)
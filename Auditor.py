'''Initialize Inventory to 0

run a loop asking enter stock quantity untill type quit

accept stock as integer

handle invalid input etc ten

reject nagtive number

keep inventory updated 

if inventory > 500, alert and break loop

when type quit, print total unit processed and numbe failed rejected entries'''

inventory = 0
quantity = 0
rejects = 0
processed = 0
#quantity = int(input("Whats the quantity of the stock"))

while True: 
    Entry = input("Whats the quantity of the stocks (or type 'quit' to quit): ")

    if Entry.lower() == "quit":
        Report = (f"Total unit processed: {processed} Number of failed/Rejected Entries: {rejects}")
        print(str(Report))
        break

    if not Entry.isdigit():
        print("Error please return whole number")
        rejects += 1
        continue
    quantity = int(Entry)

    if quantity < 0:
        rejects += 1
        continue

    inventory += quantity
    processed += 1

    if inventory > 500:
        print("!!! exceeded 500 unit !!!")
        break
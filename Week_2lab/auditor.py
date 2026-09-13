'''Initialize Inventory to 0

run a loop asking enter stock quantity untill type quit

accept stock as integer

handle invalid input etc ten

reject nagtive number

keep inventory updated 

if inventory > 500, alert and break loop

when type quit, print total unit processed and numbe failed rejected entries'''

inventory = 0
rejects = 0

while True:
    Entry = input("Enter stock quantity:")

    if Entry == "quit":
        print("Total unit processed:", inventory)
        print("Number of rejects:", rejects)
        break
    elif not Entry.isdigit():
            print("Error please enter whole number")
            rejects += 1
            continue

    quantity = int(Entry)

    if int(Entry) < 0:
            print("No negative number")
            rejects += 1
            continue

    inventory += int(quantity)

    
    if inventory > 500:
        print("!!! Alert !!! exceed 500 unit")
        break
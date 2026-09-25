inventory = 0
rejects = 0
delivery = 0
history = []

def load_inventory():
    global inventory, history
    try:
        with open("inventory.txt", "r") as f:
            lines = f.readlines()
            inventory = int(lines[0].strip())
            transaction_lines = lines[1:]
            history = []
            for line in transaction_lines:
                 clean = line.strip()
                 amount = int(clean)
                 history.append(amount)
            # next: figure out total and history from `lines`
    except FileNotFoundError:
        inventory = 0
        history = []

def save_inventory(total, transactions):
    with open("inventory.txt", "w") as f:
        f.write(str(total) + "\n")          # <- this runs FIRST
        for amount in transactions:          # <- this runs AFTER
            f.write(str(amount) + "\n")

def get_valid_input():
        global inventory
        global rejects
        Entry = input("Enter Stock Quantity:")

        if Entry == "quit":
             return Entry

        try:
             num = int(Entry)
             if num > 0:
                  inventory = process_delivery(inventory, int(Entry))
                  history.append(num)
                  print(inventory)
                  # 1 unit is $10 
                  delivery_amount = inventory * 10
                  tax = calculate_tax(delivery_amount)
                  print("$",delivery_amount) 
                  if inventory > 500:
                        print("Alert exceed 500 units")
                        return inventory

             elif num < 0:
                  print("no negative number")
                  rejects += 1
        
        except(ValueError):
             print("Error please enter whole number")    
             rejects += 1
             print(rejects)

            
def process_delivery(current_total, new_value):
       return current_total + new_value



def calculate_tax(amount):
       return amount * 0.10

def generate_report(total_unit, failed_attempts):
    print(f"Total Deliveries Processed: {total_unit}")
    print(f"Number of Failed/Rejected Entries: {failed_attempts}")      



load_inventory()

#while True:

#    result = get_valid_input() 
#    if result == "quit":
 #         generate_report(inventory,rejects)
 #         break
 #   elif inventory > 500:
 #       break
    
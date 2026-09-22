
inventory = 0
rejects = 0
delivery = 0

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
                  print(inventory)
                  # 1 unit is $10 
                  delivery_amount = inventory * 10
                  tax = calculate_tax(delivery_amount)
                  print("$",delivery_amount) 

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

while True:

    result = get_valid_input() 
    if result == "quit":
          generate_report(inventory,rejects)
          break
    
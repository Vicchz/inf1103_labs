import json
stocks = 0
price = 0

starter_inventory = [
    {"ID": "P001", "Name": "Laptop", "Price": 1200.00, "Stocks": 15},
    {"ID": "P002", "Name": "Mouse", "Price": 25.50, "Stocks": 40},
    {"ID": "P003", "Name": "Keyboard", "Price": 45.00, "Stocks": 25}
]

def load_inventory():
    try:    
        with open("inventory.json", "r") as file: 
            inventory = json.load(file)
            print("inventory.json found.\nInventory loaded successfully")
    except FileNotFoundError:
        print("missing file")
        inventory = starter_inventory

    return inventory

def display_all(inventory):
    print("Current Inventory")
    print("-------------------------------")
    for item in inventory:
        print(f"ID: {item['ID']} | Name: {item['Name']} | Price: {item['Price']:.2f} | Stock: {item['Stocks']}")
    print("-------------------------------")


def save_inventory(product):
    with open("inventory.json", "w") as file:
        print("Saving inventory...")
        json.dump(product, file, indent=4)
    print("Inventory saved successfully to inventory.json")

def add_product(inventory):
    product_id = input("ID:")
    name = input("Name:")
    price = float(input("Price: "))
    stocks = int(input("stocks:"))
    new_product = {
         "ID": product_id,  "Name": name, "Price": price, "Stocks": stocks
    }
    inventory.append(new_product)
    print("Product added successfully!")

def search_product(inventory, pid):
    for item in inventory:
        if item["ID"] == pid:
            return item
    return None

def update_stock(inventory):
    pid = input("Enter Product ID: ")
    item = search_product(inventory, pid)
    if item is None:
        print("Product not found.")
    else:
        print("Product Found:")
        print(f"Name: {item['Name']}")
        print(f"Current Stock: {item['Stocks']}")
        item["Stocks"] = int(input("New Stock Quantity: "))
        print("Stock updated successfully!")

def Menu_system():
    while True:
        print("-----------MENU------------")
        print("1. Display All Producsts \n2. Add Product \n3. Update Stock \n4. Search Product \n5. Save Inventory \n6. Exit")
        print("---------------------------")
        choice = int(input("Enter option:"))
        if (choice == 1):
            display_all(inventory)
        elif (choice == 2):
            add_product(inventory)
        elif (choice == 3):
            print("Update stock") #not done defupdate stock
            update_stock(inventory)

        elif(choice == 4):
            print("search product")
            pid = input("Enter Product ID: ")
            item = search_product(inventory, pid)
            if item is None:
                print("Product not found")
            else:
                print("Product Found.")
                print("-" * 48)
                print(f"ID: {item['ID']}")
                print(f"Name: {item['Name']}")
                print(f"Price: {item['Price']:.2f}")
                print(f"Stock: {item['Stocks']}")
                print("-" * 48)

        elif(choice == 5):
            save_inventory(inventory)
        elif(choice == 6):
            print("Saving inventory before exit...")
            print("Inventory saved successfully.")
            print("\nThank you for using Inventory Managament System.\nProgram terminated")
            break

inventory = load_inventory()
print("=" * 48)
print("INVENTORY MANAGEMENT SYSTEM")
print("=" * 48)
Menu_system()
#add_product(inventory)
#print(inventory)
#search_product(inventory, pid = input("Enter Product ID:"))
#display_all(inventory)
#save_inventory(inventory)



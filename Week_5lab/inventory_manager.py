import json
stocks = 0
price = 0

inventory = [
    {"ID:": "P001", "Name:": "Laptop", "Price: $": price, "Stocks:": stocks},
    {"ID:": "P002", "Name:": "Mouse", "Price: $": price, "Stocks:": stocks},
    {"ID:": "P003", "Name:": "Keyboard", "Price: $": price, "Stocks:": stocks}
]

def load_inventory():
    try:
        with open("inventory.json", "r") as file: 
            inventory = json.load(file)
            print("inventory.json found.\nInventory loaded successfully")
    except FileNotFoundError:
        print("missing file")
        inventory = []

    return inventory

def display_all(inventory):
    print("Current Inventory")
    print("-------------------------------")
    for item in inventory:
        print(f"ID: {item['id']} | Name: {item['name']} | Price: ${item['price']:.2f} | Stock: {item['Stocks']}")
    print("-------------------------------")


inventory = load_inventory()

display_all(inventory)



import json
from iventory import Inventory
from retry import Product


def load_inventory():
    inventory = Inventory()
    with open("inventory.json", "r") as file:
        data = json.load(file)
        print("inventory.json found.")
    for item in data:
        inventory.add_product(Product(item["ID"], item["Name"], item["Price"], item["Stocks"]))
    print("Inventory loaded successfully")
    return inventory

def save_inventory(inventory):
    data = [product.to_dict() for product in inventory.get_products()]
    with open("inventory.json", "w") as file:
        json.dump(data, file, indent=4)
    print("Inventory saved successfully to inventory.json")


def menu_system(inventory):
    while True:
        print("\n-----------MENU------------")
        print("1. Display All Products\n2. Add Product\n3. Update Stock\n4. Search Product\n5. Save Inventory\n6. Exit")
        print("---------------------------")
        choice = int(input("Enter option: "))

        if choice == 1:
            inventory.display_all()
        elif choice == 2:
            pid = input("ID: ")
            name = input("Name: ")
            price = float(input("Price: "))
            stock = int(input("Stocks: "))
            inventory.add_product(Product(pid, name, price, stock))
            print("Product added successfully!")
        elif choice == 3:
            product = inventory.search_product(input("Enter Product ID: "))
            if product is None:
                print("Product not found.")
            else:
                print(f"Name: {product.name}")
                print(f"Current Stock: {product.stock}")
                product.update_stock(int(input("New Stock Quantity: ")))
                print("Stock updated successfully!")
        elif choice == 4:
            product = inventory.search_product(input("Enter Product ID: "))
            if product is None:
                print("Product not found.")
            else:
                product.display_information()
        elif choice == 5:
            save_inventory(inventory)
        elif choice == 6:
            save_inventory(inventory)
            print("Program terminated")
            break

inventory = load_inventory()
menu_system(inventory)
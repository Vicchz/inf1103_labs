import json
from Physical_product import PhysicalProduct
from Digital_product import DigitalProduct
from inventory import Inventory

def load_inventory():
    inventory = Inventory()
    with open("inventory.json", "r") as file:
        data = json.load(file)
        print(len(data))
    for item in data:
        if item["type"] == "physical":
            product = PhysicalProduct(item["ID"], item["Name"], item["Price"], item["Stocks"], item["weight"])
        else:
            product = DigitalProduct(item["ID"], item["Name"], item["Price"], item["Stocks"], item["download_size"])
        inventory.add_product(product)
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
            kind = input("Type (physical/digital): ")
            if kind == "physical":
                print("build physical")
                weight = float(input("Weight (kg): "))
                product = PhysicalProduct(pid, name, price, stock, weight)
            else:
                size = float(input("Download size (MB): "))
                product = DigitalProduct(pid, name, price, stock, size)
            inventory.add_product(product)
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



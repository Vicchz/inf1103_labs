import json

starter_inventory = [
    {"ID": "P001", "Name": "Laptop", "Price": 1200.00, "Stocks": 15},
    {"ID": "P002", "Name": "Mouse", "Price": 25.50, "Stocks": 40},
    {"ID": "P003", "Name": "Keyboard", "Price": 45.00, "Stocks": 25}
]

class Product:


    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    @property
    def product_id(self):
        return self.__product_id

    @property
    def name(self):
        return self.__name

    @property
    def stock(self):
        return self.__stock

    def to_dict(self):
        return {"ID": self.__product_id, "Name": self.__name,
                "Price": self.__price, "Stocks": self.__stock}
    
    def update_stock(self, quantity):
        if quantity < 0:
            return False
        self.__stock = quantity
        return True
        

    def display_information(self):
        print(f"ID:{self.__product_id} | Name:{self.__name} | Price:{self.__price} | Stock:{self.__stock}")


product = Product("P001", "Laptop", "1200", "15")    
#product.updatestock()
product.display_information()
product.update_stock(50)
product.display_information()

class Inventory:
    def __init__(self):
        self.__products = []          

    def add_product(self, product):
        self.__products.append(product)

    def get_products(self):
        return list(self.__products)

    def search_product(self, product_id):
        for product in self.__products:
            if product.product_id == product_id:
                return product
        return None

    def display_all(self):
        for product in self.__products:
            product.display_information()

def load_inventory():
    inventory = Inventory()
    with open("inventory.json", "r") as file:
        data = json.load(file)
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
        print("-----------MENU------------")
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
print("=" * 48)
print("INVENTORY MANAGEMENT SYSTEM")
print("=" * 48)
menu_system(inventory)
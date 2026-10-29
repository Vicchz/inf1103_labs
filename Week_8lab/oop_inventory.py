class Product:


    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    @property
    def product_id(self):
        return self.__product_id
    
    def updatestock(self, quantity):
        if quantity < 0:
            return False
        self.__stock = quantity
        return True
        

    def display_information(self):
        print(f"ID:{self.__product_id} | Name:{self.__name} | Price:{self.__price} | Stock:{self.__stock}")


product = Product("P001", "Laptop", "1200", "15")    
#product.updatestock()
product.display_information()
product.updatestock(50)
product.display_information()

class Inventory:
    def __init__(self):
        self.__products = []          # empty list = empty shelf

    def add_product(self, product):
        self.__products.append(product)

    def search_product(self, product_id):
        for product in self.__products:
            if product.product_id == product_id:
                return product
        return None

    def display_all(self):
        for product in self.__products:
            product.display_information()


inventory = Inventory()
inventory.add_product(Product("P001", "Laptop", 1200.00, 15))
inventory.add_product(Product("P002", "Mouse", 25.50, 50))
inventory.display_all()                  # shows both products
inventory.search_product("P002").display_information()   # shows Mouse
print(inventory.search_product("P002"))  # None
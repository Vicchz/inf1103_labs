class Product:


    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

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

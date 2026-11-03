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
    def price(self):
        return self.__price

    @property
    def stock(self):
        return self.__stock

    def update_stock(self, quantity):
        if quantity < 0:
            return False
        self.__stock = quantity
        return True

    def to_dict(self):
        return {"ID": self.__product_id, "Name": self.__name, "Price": self.__price, "Stocks": self.__stock}

    def display_information(self):
        print(f"ID:{self.__product_id} | Name:{self.__name} | Price:{self.__price} | Stock:{self.__stock}")


if __name__ == "__main__":
    product = Product("999", "monitor", 2500, 25)
    product.display_information()

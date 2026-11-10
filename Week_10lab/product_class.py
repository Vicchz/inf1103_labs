from supplier import Supplier
from abc import ABC, abstractmethod


class Product(ABC):

    def __init__(self, product_id, name, price, stock, supplier:Supplier):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock
        self.__supplier: Supplier = supplier
    @abstractmethod
    def get_fufillment_info(self):
        pass

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

    @property
    def supplier(self):
        return self.__supplier

    def update_stock(self, quantity):
        if quantity < 0:
            return False
        self.__stock = quantity
        return True

    def to_dict(self):
        return {"ID": self.__product_id, "Name": self.__name, "Price": self.__price, "Stocks": self.__stock}

    def display_information(self):
        print(f"ID:{self.__product_id} | Name:{self.__name} | Price:{self.__price} | Stock:{self.__stock}")


from product_class import Product
from can_be_ship import CanBeShipped

class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self.__weight = weight

    def display_information(self):
        super().display_information()
        print(f"Weight: {self.__weight}kg")

    
    def get_fufillment_info(self):
        return "Need Physical Shipping"

    def calculate_shipping_cost(self):
        return self.__weight * 5

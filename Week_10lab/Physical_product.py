from supplier import Supplier
from product_class import Product
from can_be_ship import CanBeShipped

class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id, name, price, stock, weight, supplier: Supplier):
        super().__init__(product_id, name, price, stock, supplier)
        self.__weight = weight

    def display_information(self):
        super().display_information()
        print(f"Weight: {self.__weight}kg")

    
    def get_fufillment_info(self):
        return "Need Physical Shipping"

    def calculate_shipping_cost(self):
        return self.__weight * 5

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "physical"
        data["weight"] = self.__weight
        return data


#s = Supplier("S1", "Acme", "acme@example.com")
#p = PhysicalProduct("P1", "Pen", 2, 5, 2, s)
#print(p.to_dict())
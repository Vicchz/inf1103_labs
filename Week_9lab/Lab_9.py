from product_class import Product

class PhysicalProduct(Product):
    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self.__weight = weight

    def display_information(self):
        super().display_information()
        print(f"Weight: {self.__weight}kg")


if __name__ == "__main__":
    p = PhysicalProduct("P1", "Pen", 2, 5, 0.1)
    p.display_information()
from product_class import Product

class Inventory:
    def __init__(self):
        self.__products: list[Product] = []

    def add_product(self, product: Product) -> None:
        self.__products.append(product)

    def get_products(self):
        return list(self.__products)

    def find_product(self, product_id) -> str | None:
        for product in self.__products:
            if product.product_id == product_id:
                return product
        return None

    def display_all(self) -> None:
        for product in self.__products:
            product.display_information()

    def remove_product(self, product_id: str) -> None:
        for product in self.__products:
            if product.product_id == product_id:
                self.__products.remove(product)
                return 


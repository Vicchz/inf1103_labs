from product_class import Product
from supplier import Supplier

class DigitalProduct(Product):
    def __init__(self, product_id, name, price, stock, download_size, supplier: Supplier):
        super().__init__(product_id, name, price, stock, supplier)
        self.__download_size = download_size

    def display_information(self):
        super().display_information()
        print(f"Download Size: {self.__download_size}MB")

    def get_fufillment_info(self):
        return "Delivered Digitally"

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "digital"
        data["download_size"] = self.__download_size
        return data


#s =  Supplier("S1", "Acme", "acme@example.com")
#if __name__ == "__main__":
    #d = DigitalProduct("P2", "Game", 30, 100, 500, s)
    #print(d.to_dict())
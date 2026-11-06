from product_class import Product

class DigitalProduct(Product):
    def __init__(self, product_id, name, price, stock, download_size):
        super().__init__(product_id, name, price, stock)
        self.download_size = download_size

    def display_information(self):
        super().display_information()
        print(f"Download Size: {self.download_size}MB")

    def get_fufillment_info(self):
        return "Delivered Digitally"


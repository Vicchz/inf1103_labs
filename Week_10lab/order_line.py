from product_class import Product

class OrderLine():
    def __init__(self, product: Product, quantity: int) -> None:
        self.product: Product = product
        self.quantity = quantity

    def calculate_subtotal(self) -> float:
        return self.product.price * self.quantity
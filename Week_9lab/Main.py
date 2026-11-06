from Physical_product import PhysicalProduct
from Digital_product import DigitalProduct


p = PhysicalProduct("P1", "Pen", 2, 5, 2)
p.display_information()
print(p.get_fufillment_info())
print(p.calculate_shipping_cost())


d = DigitalProduct("P2", "Game", 30, 100, 500)
d.display_information()
print(d.get_fufillment_info())
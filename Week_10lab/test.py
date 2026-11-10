from supplier import Supplier
from Physical_product import PhysicalProduct  
from Digital_product import DigitalProduct    
from inventory import Inventory
from order_line import OrderLine
from order import Order
from product_class import Product

def show_found(label: str, product: Product | None) -> None:
    """Print a product's id, or None if it was not found."""
    print(label, product.product_id if product else None)
 
 
def show_product_details(product: Product) -> None:
    """Works for ANY Product: this is polymorphism + LSP."""
    product.display_information()
    print(product.get_fufillment_info())
 
 
print("\n--- Step 1: association ---")
s = Supplier("S1", "Acme", "acme@example.com")
p1 = PhysicalProduct("P1", "Pen", 2, 5, 2, s)
p2 = DigitalProduct("D100", "GTA9", 99, 1, 3000, s)
 
p1.supplier.display_information()
p2.supplier.display_information()
 
del s
p1.supplier.display_information()
p2.supplier.display_information()
 
 
print("\n--- Step 2: aggregation ---")
inv_a = Inventory()
inv_b = Inventory()
 
inv_a.add_product(p1)
show_found("In A:", inv_a.find_product("P1"))
 
inv_a.remove_product("P1")
show_found("In A after remove:", inv_a.find_product("P1"))
 
p1.display_information()          
 
inv_b.add_product(p1)
show_found("In B:", inv_b.find_product("P1"))
 
 
print("\n--- Step 3: composition ---")
pen = p1
book = p2
 
order1 = Order("O1")
order1.add_order_line(pen, 3)
order1.add_order_line(book, 1)
 
for line in order1.order_lines:
    print(line.product.product_id, line.quantity, line.calculate_subtotal())
print("Total:", order1.calculate_total())
 
order2 = Order("O2")
order2.add_order_line(pen, 2)
 
print("Same OrderLine object?", order1.order_lines[0] is order2.order_lines[0])
print("Same Product object?  ", order1.order_lines[0].product is order2.order_lines[0].product)
 
del order1
pen.display_information()
 
 
print("\n--- Step 5: polymorphism ---")
inv = Inventory()
inv.add_product(p1)      # PhysicalProduct
inv.add_product(p2)      # DigitalProduct
 
show_product_details(p1)
show_product_details(p2)
 
print()
for product in inv.get_products():     
    show_product_details(product)
 
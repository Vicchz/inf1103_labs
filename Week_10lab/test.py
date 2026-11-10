from supplier import Supplier
from Physical_product import PhysicalProduct  
from Digital_product import DigitalProduct    
from inventory import Inventory
from order_line import OrderLine
from order import Order

s = Supplier("S1", "Acme", "acme@example.com")
p1 = PhysicalProduct("P300","Mouse", 39.99, 3, 1.2, s)    
p2 = DigitalProduct("D100","GTA9", 99,"1", 3000, s)


inv_a = Inventory()
inv_b = Inventory()


p1 = PhysicalProduct("P1", "Pen", 2, 5, 2, s)

inv_a.add_product(p1)
print("In A:", inv_a.find_product("P1"))      

inv_a.remove_product("P1")
print("In A after remove:", inv_a.find_product("P1"))   

p1.display_information()

inv_b.add_product(p1)
print("In B:", inv_b.find_product("P1"))

# --- Step 3: composition ---
pen = p1                                  # reuse your Physical product
book = p2                                 # reuse your Digital product

order1 = Order("O1")
order1.add_order_line(pen, 3)
order1.add_order_line(book, 1)

for line in order1.order_lines:
    print(line.product.product_id, line.quantity, line.calculate_subtotal())
print("Total:", order1.calculate_total())

# same Product into a second Order
order2 = Order("O2")
order2.add_order_line(pen, 2)

print("Same OrderLine object?", order1.order_lines[0] is order2.order_lines[0])
print("Same Product object?  ", order1.order_lines[0].product is order2.order_lines[0].product)
from supplier import Supplier
from Physical_product import PhysicalProduct  
from Digital_product import DigitalProduct    
from inventory import Inventory

s = Supplier("S1", "Acme", "acme@example.com")
p1 = PhysicalProduct("P300","Mouse","39.99","3", "1.2", s)    
p2 = DigitalProduct("D100","GTA9","99","1", "3000", s)

# --- Step 2: aggregation ---
inv_a = Inventory()
inv_b = Inventory()

# 1. Product exists BEFORE any inventory
p1 = PhysicalProduct("P1", "Pen", 2, 5, 2, s)

# 2. Add to A
inv_a.add_product(p1)
print("In A:", inv_a.find_product("P1"))      # should show the product

# 3. Remove from A
inv_a.remove_product("P1")
print("In A after remove:", inv_a.find_product("P1"))   # should be None

# 4. Product still works on its own
p1.display_information()

# 5. Same object goes into B
inv_b.add_product(p1)
print("In B:", inv_b.find_product("P1"))
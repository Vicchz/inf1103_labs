class Supplier():
    def __init__(self, supplier_id, name, contact_email):
        self.supplier_id = supplier_id
        self.name = name
        self.contact_email = contact_email

    def display_information(self):
        print(f"ID:{self.supplier_id} | Name: {self.name} | Contact: {self.contact_email}")


if __name__ == "__main__":
    s = Supplier("S1", "Acme", "acme@example.com")
    s.display_information()
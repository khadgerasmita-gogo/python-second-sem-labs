class Laptop:
    def __init__(self, brand, model, ram):
        self.brand = brand
        self.model = model
        self.ram = ram

# Instantiate two different laptop objects
laptop1 = Laptop("Dell", "Inspiron 15", 8)
laptop2 = Laptop("HP", "Pavilion x360", 16)

# Print their attributes
print("Laptop 1:")
print("Brand:", laptop1.brand)
print("Model:", laptop1.model)
print("RAM:", laptop1.ram, "GB")

print("\nLaptop 2:")
print("Brand:", laptop2.brand)
print("Model:", laptop2.model)
print("RAM:", laptop2.ram, "GB")

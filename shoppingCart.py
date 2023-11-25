class Product:
    def __init__(self, name, unit_price, gst_percentage, quantity):
        self.name = name
        self.unit_price = unit_price
        self.gst_percentage = gst_percentage
        self.quantity = quantity

    def calculate_total_price(self):
        return self.unit_price * self.quantity * (1 + self.gst_percentage / 100)

# Creating products in the basket
products = [
    Product("Leather wallet", 1100, 18, 1),
    Product("Umbrella", 900, 12, 4),
    Product("Cigarette", 200, 28, 3),
    Product("Honey", 100, 0, 2)
]

# Calculate total amount to be paid to the shopkeeper
total_amount = sum(product.calculate_total_price() for product in products)

# Identify the product for which the maximum GST amount is paid
max_gst_product = max(products, key=lambda x: x.unit_price * x.quantity * x.gst_percentage / 100)

# Displaying results
print("Total amount to be paid to the shopkeeper:", total_amount)
print("Product with the maximum GST amount paid:", max_gst_product.name)

products = {
    "Laptop": 10,
    "Mouse": 25,
    "Keyboard": 15
}

print("Stock Details")

for product, qty in products.items():
    print(product, "- Quantity:", qty)
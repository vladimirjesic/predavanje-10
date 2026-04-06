from methods import load_file, save_file

products = load_file("data/products.json")
print(products)
products.append({
    "name": "Joystick",
    "price": 80,
    "amount": 5
})
save_file("data/products.json", products)
print(products)
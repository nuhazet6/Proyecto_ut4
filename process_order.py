def process_order(code, quantity, money):
    product = products.get(code)
    if product:
        if quantity > product["stock"]:
            return "E2"
        else:
            total_cost = product["price"] * quantity
            if money > total_cost:
                product["stock"] -= quantity
            else:
                return "E3"
    else:
        return "E1"


products = {"K20": {"stock": 5, "price": 1}}
machine = {"money": 100}
print(machine)
print(products)
process_order("K20", 4, 10)
print(products)

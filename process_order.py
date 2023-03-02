def money_change(movement: int, current: int):
    current += movement


def process_order(code, quantity, money):
    product = products.get(code)
    if product:
        if quantity > product["stock"]:
            return "E2"
        else:
            total_cost = product["price"] * quantity
            if money > total_cost:
                money_change(total_cost, machine_money)
                product["stock"] -= quantity
            else:
                return "E3"
    else:
        return "E1"


products = {"K20": {"stock": 5, "price": 1}}
machine_money = 100

print(products, machine_money)
process_order("K20", 4, 10)
print(products, machine_money)

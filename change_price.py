def change_price(code: str, price: int, machine_products: dict):
    if code in machine_products:
        machine_products[code]["price"] = price
        error = 0
    else:
        error = 1
    return error

def change_price(code: str, price: int):
    if code in products:
        products[code]["price"] = price
        error = 0
    else:
        error = "E1"
    return error

def change_price(code: str, price: float):
    if code in products:
        products[code]["price"] = price
        error = 0
    else:
        error = "E1"
    return error


with open("vending.dat", "r") as f:
    TYPE_COIN = [2, 1, 0.5]
    coins = {
        coin_type: float(coin)
        for coin_type, coin in zip(TYPE_COIN, f.readline().strip().split())
    }
    products = {}
    for line in f:
        info_product = line.strip().split()
        code = info_product[0]
        stock = int(info_product[1])
        price = float(info_product[2])
        products[code] = {"stock": stock, "price": price}

print(products)
print(change_price("D31", 1.0))
print(products)
print(change_price("DKK", 1.0))

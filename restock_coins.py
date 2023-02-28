# initialize
money = 0
products = {}


def recharge_money(amount: int):
    money += amount

    money = int(f.readline())
    products = {}
    for line in f:
        info_product = line.strip().split()
        code = info_product[0]
        stock = int(info_product[1])
        price = float(info_product[2])
        products[code] = {"stock": stock, "price": price}


print(money)
recharge_money(100)
print(money)

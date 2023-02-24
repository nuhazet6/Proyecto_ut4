with open("vending.dat", "r") as f:
    TYPE_COIN = [2, 1, 0.5]
    coins = {
        type: float(coin) for type, coin in zip(TYPE_COIN, f.readline().strip().split())
    }
    products = {}
    for line in f:
        info_product = line.strip().split()
        code = info_product[0]
        stock = int(info_product[1])
        price = float(info_product[2])
        products[code] = {"stock": stock, "price": price}

with open("operations.dat", "r") as f:
    orders = []
    codes = set()
    for line in f:
        info_envio = line.strip().split()
        order_type = info_envio[0]
        code = info_envio[1]
        amount = int(info_envio[2])
        money = [int(i) for i in info_envio[3:]]
        orders.append((order_type, code, amount, money))
print(products, coins)


def price(code):
    info = products.get(code, {"ERROR": -1})
    price = list(info.items()[0])
    return price


def stock(code):
    info = products.get(code, {None: None, "ERROR": -2})
    stock = list(info.items())[1]
    return stock


print(stock("D31"))


def buy(*, code, amount, money):
    return 0

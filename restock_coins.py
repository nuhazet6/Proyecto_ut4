def restock_coins(amounts: list):
    for coin_type, amount in zip(TYPE_COIN, amounts):
        coins[coin_type] += amount
    return None


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

print(coins)
restock_coins([5, 5, 5])
print(coins)

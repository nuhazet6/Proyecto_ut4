products = {"K20": {"stock": 5, "price": 1}}


def restock_product(code, amount):
    if code in products:
        products[code]["stock"] += amount
    else:
        products[code] = {"stock": amount, "price": 0}


print(products)
restock_product("K20", 5)
print(products)
restock_product("K90", 6)
print(products)

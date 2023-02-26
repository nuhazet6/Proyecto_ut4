with open("vending.dat", "r") as f:
    TYPE_COIN = [2, 1, 0.5]
    coins = {
        coin_type: float(coin) for coin_type, coin in zip(TYPE_COIN, f.readline().strip().split())
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
    for line in f:
        info_envio = line.strip().split()
        orders.append(info_envio)

def get_price(code):
    info = products.get(code, {})
    price = info.get('price', -1)#ERROR: -1
    return price

def get_stock(code):
    info = products.get(code, {})
    stock = info.get('stock', -2)#ERROR: -2
    return stock

def get_coin(coin_type):
    return  coins.get(coin_type, -3)

def change_coins(change):
    change_amnts = {}
    for coin_type in TYPE_COIN:
        change_amnts[coin_type] = change // coin_type 
        if change_amnts[coin_type] > coins[coin_type]:
            change_amnts[coin_type] = coins[coin_type]#logica de devolución?
        change -= change_amnts[coin_type]
    return change_amnts
    
def do_order(operation_data):
    code, quant, *amnt_coins = operation_data
    price = get_price(code)
    stock = get_stock(code)
    payed = sum([value*int(amnt) for value,amnt in zip(TYPE_COIN,amnt_coins)])
    for coin_type,amnt in zip(TYPE_COIN, amnt_coins):
        coins[coin_type] += amnt   
    change = payed - price * quant#antes o después de introducir sus monedas en el balance?
    change_amnts = change_coins(change)
    change = (change == sum([k*v for k,v in change_amnts.items()]))-1#hacerselo mirar(dejarla por ahí en cualquier caso)
    stock_movement = stock - quant
    error_catched = '-' in (str(price) + str(stock) + str(change) + str(stock_movement))#función? n argumentos iterados y sumados como str
    if error_catched:
        for coin_type,amnt in zip(TYPE_COIN, amnt_coins):
            coins[coin_type] -= amnt 
    else:
        change_amnts = change_coins(change)
        for coin_type in (TYPE_COIN):
            coins[coin_type] -= change_amnts[coin_type]
    return 

for order in orders:
    operation_type, operation_data = order[0], order[1:]
    match operation_type:
        case 'O':
        case 'R':
        case 'P':
        case 'C':
        case _: #capturar error de operación no soportada

#recarga de producto  N
#cambio precio  J
#recarga monedas  J
#salida N
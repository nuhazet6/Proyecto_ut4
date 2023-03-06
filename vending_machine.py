<<<<<<< HEAD
def restock_product(code: str, quantity: int, machine_products: dict):
    if code in machine_products:
        machine_products[code]["stock"] += quantity
    else:
        machine_products[code] = {"stock": quantity, "price": 0}


def change_price(code: str, price: int, machine_products: dict):
    if code in machine_products:
        machine_products[code]["price"] = price
        error = None
    else:
        error = "E1"
    return error
=======
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
        amount = float(info_envio[2])
        money = [float(i) for i in info_envio[3:]]
        orders.append((order_type, code, amount, money))
print(products, coins)


def price(code):
    info = products.get(code, {"ERROR": -1})
    price = info.items()[0]
    return price
>>>>>>> f03d129d59c1822cc0ed22a2d4d5f68515e0ef7c


def money_movement(movement: int, machine_status: dict):
    machine_status["machine_money"] += movement


def process_order(code: str, quantity: int, money: int, machine_status: dict):
    product = machine_status["machine_products"].get(code)
    if product:
        if quantity > product["stock"]:
            return "E2"
        else:
            total_cost = product["price"] * quantity
            if money > total_cost:
                money_movement(total_cost, machine_status)
                product["stock"] -= quantity
            else:
                return "E3"
    else:
        return "E1"


# los productos se van introduciendo y eliminando según toque, el dinero se modifica el valor
machine_status = {"machine_money": 0, "machine_products": {}}
with open("operations.dat", "r") as f:
    for row in f:
        operation_type, *operation_data = row.split()
        match operation_type:
            case "M":
                movement = int(operation_data[0])
                money_movement(movement, machine_status)
            case "O":
                code, quantity, money = operation_data
                quantity = int(quantity)
                money = int(money)
                process_order(code, quantity, money, machine_status)
            case "R":
                code, quantity = operation_data
                quantity = int(quantity)
                restock_product(code, quantity, machine_status["machine_products"])
            case "P":
                code, price = operation_data
                price = int(price)
                change_price(code, price, machine_status["machine_products"])
            case _:
                print("Operación no reconocida, lo lamentamos.")
# en este punto el diccionario guarda del estado de la máquina, falta formatear la salida:
# ordenar los productos
machine_status["machine_products"] = dict(
    sorted(machine_status["machine_products"].items(), key=lambda t: t[0])
)
# formateado para la salida
with open("status.dat", "w") as f:
    money = str(machine_status["machine_money"])
    f.write(f"{money}\n")
    for product_code, product_data in machine_status["machine_products"].items():
        stock, price = product_data["stock"], product_data["price"]
        f.write(f"{product_code} {stock} {price}\n")

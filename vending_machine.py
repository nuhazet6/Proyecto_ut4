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

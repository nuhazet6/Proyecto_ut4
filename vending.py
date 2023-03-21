# ******************
# MÁQUINA DE VENDING
# ******************
import filecmp
from pathlib import Path

ERROR_DESCRIPTIONS = {
    "E1": "Product not found",
    "E2": "Unavailable stock",
    "E3": "Not enough user money",
}


def restock_product(code: str, quantity: int, products: dict):
    if code in products:
        products[code]["stock"] += quantity
    else:
        products[code] = {"stock": quantity, "price": 0}


def change_price(code: str, price: int, products: dict) -> (str | None):
    if code in products:
        products[code]["price"] = price
        return None
    return "E1"


def money_movement(movement: int, machine_status: dict) -> None:
    machine_status["money"] += movement


def process_order(
    code: str, quantity: int, money: int, machine_status: dict
) -> (str | None):
    if product_data := machine_status["products"].get(code):
        if quantity > product_data["stock"]:
            return "E2"
        else:
            total_cost = product_data["price"] * quantity
            if money >= total_cost:
                money_movement(total_cost, machine_status)
                product_data["stock"] -= quantity
                return None
            else:
                return "E3"
    else:
        return "E1"


def run(operations_path: Path) -> bool:
    status_path = "data/vending/status.dat"
    # los productos se van introduciendo y eliminando según toque, el dinero se modifica el valor
    machine_status = {"money": 0, "products": {}}
    with open(operations_path, "r") as f:
        operations = f.readlines()
    for operation in operations:
        error_code = None
        operation_type, *operation_args = operation_data = operation.split()
        match operation_type:
            case "M":
                movement = int(operation_args[0])
                money_movement(movement, machine_status)
            case "O":
                code, quantity, money = operation_args
                quantity = int(quantity)
                money = int(money)
                error_code = process_order(code, quantity, money, machine_status)
            case "R":
                code, quantity = operation_args
                quantity = int(quantity)
                restock_product(code, quantity, machine_status["products"])
            case "P":
                code, price = operation_args
                price = int(price)
                error_code = change_price(
                    code, price, machine_status["products"]
                )
            case _:
                print("Operación no reconocida, lo lamentamos.")
        # salida por pantalla de la información de la operación
        if error_code:
            operation_data.append(f"{error_code}: {ERROR_DESCRIPTIONS[error_code]}")
            message = " ".join(operation_data)
            print(f"❌ {message}")
        else:
            message = " ".join(operation_data)
            print(f"✅ {message}")
    # en este punto el diccionario guarda del estado de la máquina, falta formatear la salida:
    # ordenar los productos (No quiere la estructura ordenada, solo la salida en el fichero)
    # machine_status["machine_products"] = dict(
    #     sorted(machine_status["machine_products"].items(), key=lambda t: t[0])
    # )
    # formateado para la salida
    with open(status_path, "w") as f:
        money = machine_status["money"]
        f.write(f"{money}\n")
        for product_code, product_data in sorted(machine_status["products"].items()):
            stock, price = product_data["stock"], product_data["price"]
            f.write(f"{product_code} {stock} {price}\n")

    return filecmp.cmp(status_path, "data/vending/.expected", shallow=False)


if __name__ == "__main__":
    run("data/vending/operations.dat")

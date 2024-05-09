
def mostrar_menu():
    print("Bienvenido al delivery de Sushi:")
    print("1. Pikachu Roll - $4500")
    print("2. Otaku Roll - $5000")
    print("3. Pulpo Venenoso Roll - $5200")
    print("4. Anguila Eléctrica Roll - $4800")

def calcular_precio(opcion, cantidad):
    precios = [4500, 5000, 5200, 4800]
    precio_unitario = precios[opcion - 1]
    precio_total = precio_unitario * cantidad
    return precio_total

def aplicar_descuento(precio_total, codigo):
    if codigo == "soyotaku":
        precio_total *= 0.9
        return True, precio_total * 0.1
    else:
        print("Código no válido.")
        nuevo_codigo = input("Ingrese el código de descuento o 'X' para volver al menú: ")
        if nuevo_codigo.lower() == "soyotaku":
            precio_total *= 0.9
            return True, precio_total * 0.1
        elif nuevo_codigo.lower() == "x":
            return False, 0
        else:
            return aplicar_descuento(precio_total, nuevo_codigo)

def main():
    mostrar_menu()
    pedido = [0, 0, 0, 0]
    total_productos = 0

    while True:
        opcion = int(input("Ingrese el número correspondiente al roll que desea ordenar (o '0' para finalizar): "))
        if opcion == 0:
            break

        cantidad = int(input("Ingrese la cantidad que desea ordenar: "))
        if opcion < 1 or opcion > 4:
            print("Opción inválida. Por favor, seleccione una opción válida.")
            continue

        pedido[opcion - 1] += cantidad
        total_productos += cantidad

    subtotal = 0
    for i in range(4):
        subtotal += pedido[i] * calcular_precio(i + 1, pedido[i])

    print("\nDetalle del pedido:")
    print("TOTAL PRODUCTOS:", total_productos)
    print("******************************")

    rolls = ["Pikachu Roll", "Otaku Roll", "Pulpo Venenoso Roll", "Anguila Eléctrica Roll"]
    for i in range(4):
        if pedido[i] > 0:
            print(rolls[i], ":", pedido[i])

    print("******************************")
    print("Subtotal por pagar: $", subtotal)

    codigo = input("¿Tiene un código de descuento? Ingréselo aquí (o 'X' para volver al menú): ")

    if codigo.lower() == "x":
        return

    descuento_aplicado, descuento_monto = aplicar_descuento(subtotal, codigo)

    if descuento_aplicado:
        print("Descuento por código: $", descuento_monto)
        print("TOTAL: $", subtotal - descuento_monto)
    else:
        print("TOTAL: $", subtotal)

if __name__ == "__main__":
    main()
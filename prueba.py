class Cliente:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono

    def validar_nombre(self):
        return len(self.nombre) >= 3

    def validar_telefono(self):
        return len(self.telefono) >= 8 and len(self.telefono) <= 9


class Entrega:
    def __init__(self, cliente):
        self.cliente = cliente
        self.cantidad_camiones = 0
        self.carga_total = 0

    def validar_cantidad_camiones(self):
        return self.cantidad_camiones > 0 

    def validar_carga_total(self):
        return self.carga_total > 0 and self.carga_total <= 450

    def calcular_precio(self):
        precio_camion = 765600
        precio_adicional = 1700
        precio_transporte_adicional = 100000

        precio_total = self.cantidad_camiones * precio_camion

        if self.carga_total > 450:
            exceso = self.carga_total - 450
            precio_total += exceso * precio_adicional
            precio_total += precio_transporte_adicional

        return precio_total


def ingresar_datos_cliente():
    nombre = input("Ingrese nombre del cliente: ")
    telefono = input("Ingrese teléfono de contacto: ")

    cliente = Cliente(nombre, telefono)

    while not cliente.validar_nombre() or not cliente.validar_telefono():
        print("Nombre debe tener al menos 3 letras y teléfono debe tener entre 8 y 9 dígitos.")
        nombre = input("Ingrese nombre del cliente: ")
        telefono = input("Ingrese teléfono de contacto: ")
        cliente = Cliente(nombre, telefono)

    return cliente


def menu():
    print("Menú:")
    print("1. Compra entrega camión estándar")
    print("2. Compra entrega carga específica")
    print("3. Imprimir boleta y cerrar pedido")


def main():
    cliente = ingresar_datos_cliente()
    entrega = Entrega(cliente)

    while True:
        menu()
        opcion = input("Ingrese su opción: ")

        if opcion == "1":
            cantidad_camiones = int(input("Ingrese cantidad de camiones estándar: "))
            if cantidad_camiones <= 0:
                print("La cantidad de camiones debe ser mayor a cero.")
            else:
                entrega.cantidad_camiones += cantidad_camiones
                entrega.carga_total += cantidad_camiones * (12 * 5 + 20 * 15 + 2 * 45)
        elif opcion == "2":
            cilindros_5 = int(input("Ingrese cantidad de cilindros de 5 kilos: "))
            cilindros_15 = int(input("Ingrese cantidad de cilindros de 15 kilos: "))
            cilindros_45 = int(input("Ingrese cantidad de cilindros de 45 kilos: "))
            carga = cilindros_5 * 5 + cilindros_15 * 15 + cilindros_45 * 45
            if carga < 0:
                print("La carga total debe ser mayor a cero.")
            else:
                entrega.cantidad_camiones += (carga // 450) + (1 if carga % 450 != 0 else 0)
                entrega.carga_total += carga
        elif opcion == "3":
            if not entrega.validar_cantidad_camiones():
                print("Debe ingresar al menos una entrega.")
            elif not entrega.validar_carga_total():
                print("La carga total debe ser mayor a cero y no puede exceder el límite de 450 kilos.")
            else:
                print("Cliente:", cliente.nombre)
                print("Teléfono:", cliente.telefono)
                print("Cantidad de camiones:", entrega.cantidad_camiones)
                print("Carga total:", entrega.carga_total, "kilos")
                print("Precio total:", entrega.calcular_precio(), "pesos")
                break
        else:
            print("Opción no válida. Por favor, ingrese una opción válida.")

            print("¿desea reliazar otro pedido? (si=1/ no= 2)")
            




if __name__ == "__main__":
    main()
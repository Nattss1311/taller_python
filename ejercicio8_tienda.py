class Tienda:
    def __init__(self):
        self.abierta = True  # Simulamos que está en horario de atención

    def permitir_acceso(self, cliente):
        if (cliente.tiene_membresia and self.abierta) or cliente.es_empleado:
            print("Acceso PERMITIDO para", cliente.nombre)
        else:
            print("Acceso DENEGADO para", cliente.nombre)


class Cliente:
    def __init__(self, nombre, tiene_membresia, es_empleado):
        self.nombre = nombre
        self.tiene_membresia = tiene_membresia
        self.es_empleado = es_empleado


# ----------- ZONA PRINCIPAL -----------
obj_tienda = Tienda()

while True:
    print("--- Control de Acceso ---")
    nombre = input("Ingrese nombre del cliente: ")

    mem = input("¿Tiene membresía? (s/n): ").lower() == "s"
    emp = input("¿Es empleado? (s/n): ").lower() == "s"

    obj_cliente = Cliente(nombre, mem, emp)
    obj_tienda.permitir_acceso(obj_cliente)

    opcion = input("¿Desea continuar? (s/n): ")
    if opcion.lower() != "s":
        print("Fin del sistema de control de acceso.")
        break

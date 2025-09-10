class Sensor:
    def __init__(self):
        self.temperatura = 0
        self.humedad = 0

    def leer(self):
        # aquí pedimos los valores manualmente
        self.temperatura = int(input("Ingrese temperatura (°C): "))
        self.humedad = int(input("Ingrese humedad (%): "))
        return self.temperatura, self.humedad


class AireAcondicionado:
    def __init__(self):
        self.encendido = False

    def controlar(self, temp, hum):
        if (temp > 28 and hum > 60) or temp > 30:
            self.encendido = True
        else:
            self.encendido = False

    def mostrar_estado(self):
        if self.encendido:
            print("El aire acondicionado está ENCENDIDO")
        else:
            print("El aire acondicionado está APAGADO")


# ----------- ZONA PRINCIPAL -----------
obj_sensor = Sensor()
obj_aire = AireAcondicionado()

while True:
    print("--- datos  de los  sensores ---")
    t, h = obj_sensor.leer()
    obj_aire.controlar(t, h)
    obj_aire.mostrar_estado()

    opcion = input("¿Desea continuar? (si/no): ")
    if opcion.lower() != "s":
        print("terminado........:).")
        break

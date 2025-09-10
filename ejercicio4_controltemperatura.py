import time   # para simular la espera de 5 segundos
import random # para simular lecturas del sensor

class Sensor:
    def __init__(self):
        self.temperatura = 20 

    def leerTemperatura(self):
        # temperatura cambia aleatoriamente
        self.temperatura = random.randint(5, 30)
        return self.temperatura

class SistemaControl:
    def __init__(self):
        self.estado = "Inactivo"

    def controlar(self, temperatura):
        if temperatura < 10:
            self.estado = "Calefactor encendido"
        elif 10 <= temperatura <= 25:
            self.estado = "Sistema inactivo"
        else:
            self.estado = "Ventilador encendido"
        print("Temperatura:", temperatura, "°C", self.estado)

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre

    def supervisar(self, sensor, sistema):
        temp = sensor.leerTemperatura()
        print("el usuario", self.nombre, "observa el sensor...")
        sistema.controlar(temp)


# ---------------- ZONA PRINCIPAL ---------------- #
nombre = input("Ingrese el nombre del usuario: ")
obj_usuario = Usuario(nombre)
obj_sensor = Sensor()
obj_sistema = SistemaControl()

while True:
    obj_usuario.supervisar(obj_sensor, obj_sistema)
    time.sleep(5)  # esperar 5 segundos

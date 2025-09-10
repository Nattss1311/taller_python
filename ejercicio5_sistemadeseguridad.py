class SistemadeSeguridad:
    def __init__(self):
        self.alarma_activada = False
        self.noche = True 

    def activar_alarma(self):
        self.alarma_activada = True
        print("Alarma activada")

    def desactivar_alarma(self):
        self.alarma_activada = False
        print("Alarma desactivada")

    def verificar(self):
        sensores = []
        for i in range(1, 4):
            valor = int(input("Sensor ",i, " (1 = movimiento, 0 = nada): "))
            sensores.append(valor)

        if self.alarma_activada and self.noche:
            if sum(sensores) >= 2:
                print(" Intruso detectado: Alarma SONANDO!!!!!!")
            else:
                print("Esta tranquilo :)")
        else:
            print("La alarma está desactivada o no es de noche.")


# ---------------- ZONA PRINCIPAL ---------------- #
sistema = SistemadeSeguridad()

while True:
    print("opciones para el sistema de seguridad")
    print("1. Activar alarma")
    print("2. Desactivar alarma")
    print("3. Verificar sensores")
    print("4. Salir")
    opcion = input("Elija una opción: ")

    if opcion == "1":
        sistema.activar_alarma()
    elif opcion == "2":
        sistema.desactivar_alarma()
    elif opcion == "3":
        sistema.verificar()
    elif opcion == "4":
        print("Saliendo del sistema de seguridad...")
        break
    else:
        print("Opción inválida")

class SistemaLuces:
    def __init__(self):
        self.noche = True   
        self.movimiento = False
        self.luz = "apagado"

    def verificar(self):
        if self.noche and self.movimiento:
            self.luz = "encendido"
        else:
            self.luz = "apagado"
        print("Estado de la luz:", self.luz)


# ---------------- ZONA PRINCIPAL ---------------- #
obj_sistema = SistemaLuces()

while True:
    mov = input("Hay movimiento? si/no: ")
    if mov.lower() == "si":
        obj_sistema.movimiento = True
    else:
        obj_sistema.movimiento = False

    obj_sistema.verificar()

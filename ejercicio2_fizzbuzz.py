class Fizzbuzz:
    def __init__(self, numero):
        #hay que decirle que solo se puede del 1 al 100
        self.numero=numero

    def recorrerNum(self,numero):
        if(numero%3==0 and numero%5==0):
            print("FizzBuzz")
        elif(numero%3==0):
            print("fizz")
        elif(numero%5==0):
            print("Buzz")
        else:
            print("No tiene FizzBuzz")
    
class Usuario:
    def __init__(self, nombre):
        self.nombre=nombre
    
    def usuarioFizzBuzz(self,Fizzbuzz,numero):
        print("usuario ", self.nombre, "esta haciendo el ejercicio con el num ", numero)
        Fizzbuzz.recorrerNum(numero)

#----------------------ZONA PRINCIPAL-------------#
obj_fb=Fizzbuzz(0)
nomus=input("ingrese su nombre de usuario: ")
obj_usu=Usuario(nomus)

while True:
    opcion = input("\nIngrese un número para FizzBuzz (o 'salir' para terminar): ")
    
    if opcion.lower() == "salir":
        print(" Fin del programa")
        break
    
    if opcion.isdigit():  # valida que sea número
        num = int(opcion)
        obj_usu.usuarioFizzBuzz(obj_fb, num)
    else:
        print(" Entrada inválida. Escriba un número o 'salir'.")

    


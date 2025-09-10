class Calculadora:
    def __init__(self, num1,num2):
        self.num1=num1
        self.num2=num2

    def operacion(self,num1,num2,op):
        if op == "+": print(f"Resultado: {num1+num2}")
        elif op == "-": print(f"Resultado: {num1-num2}")
        elif op == "*": print(f"Resultado: {num1*num2}")
        elif op == "/": print("Error: división por cero" if num2==0 else f"Resultado: {num1/num2}")
        else: print("Operación no válida")
       



class Usuario:
    def __init__(self,nombre):
        self.nombre=nombre
    def usuarioCalc(self,Calculadora,num1,num2,op):
        print("usuario ", self.nombre, "va a calcular una operacion con el num1 ", num1, "y el num 2 ", num2)
        Calculadora.operacion(num1,num2,op)


#-------ZONA DE OPERACION PRINCIPAL-----#
nomusu=input("ingrese nombre usuario")
obj_usu=Usuario(nomusu)
num1=int(input("Ingrese primer numero: "))
num2=int(input("Ingrese segundo numero: "))
obj_cal=Calculadora(num1,num2)
while True:
    op=input("ingrese la opcion de la operacion Operación (+ - * /): ")
    obj_usu.usuarioCalc(obj_cal,num1,num2,op)
    
    otra = input("¿Desea hacer otra operación con los mismos números? (s/n): ")
    if otra.lower() != "s":  # si no es "s", rompe el bucle
        break    





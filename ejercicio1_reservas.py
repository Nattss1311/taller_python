#ejercicio1 reservas
class Sala : 
#primero hacer constructor
    def __init__(self, capacidad):
        #creamos la lista con los asientos y recorremos por cada que ingrese de capacidad entonces
        #se va a llenar con disponible
        self.asiento=[]
        for i in range (capacidad):
            self.asiento.append("Disponible")

    def mostrarAsientos(self):
        #definimos una variable que va a ser como nuestro indice para recorrer
        i =1
        #vamos a hacer que se recorra con una variable lo que esta dentro de la lista
        #estado va a fuardar el valor de disponible (?)
        for estado in self.asiento:
            print("el asiento ", i, "esta : ", estado)
            i+=1
    
    def reservar(self, numero):
        if numero<1 or numero >len(self.asiento):
            print("invalido el numero")
            return
        #ponemos == para buscar el indice como tal y si esta disponible pues lo pasamos
        #a ocupado y en numero se guarda es el numero que digite la persona

        if self.asiento[numero-1]=="Disponible":
            self.asiento[numero-1]="Ocupado"
            print("Asiento numero ", numero, "ha sido reservado con exito")

        else:
            print("esta ocupado el asiento num ", numero)

class Usuario:
    def __init__(self, nombre):
        self.nombre=nombre

    def reservarAsiento(self, sala, numero):
        print(self.nombre, "esta intenando reserverar el asiento ", numero)
        sala.reservar(numero)

#----------------zona principal-----------------------------------------#
numerosala=int(input("ingrese cuantos asientos tendra la sala "))
obj_sala=Sala(numerosala)
nomusu=input("Ingrese el nombre de usuario")
obj_usu= Usuario(nomusu)


while True:
    obj_sala.mostrarAsientos()
    opcion = input("Ingrese número de asiento a reservar (o 'salir'): ")
    if opcion.lower() == "salir":
        break

    if opcion.isdigit():
        obj_usu.reservarAsiento(obj_sala, int(opcion))
    else:
        print("Entrada inválida.")

    if all(estado == "Ocupado" for estado in obj_sala.asiento):
        print("\nTodos los asientos están ocupados. Fin de reservas.")
        break






            

                
        
      


class Saludo:
    def __init__(self,dato_texto):
        self.mensaje=dato_texto
        print(self.mensaje)    
    def get_mensaje(self):
        return self.mensaje
    def set_atributo(self, dato_nuevo_mensaje):
        self.mensaje=dato_nuevo_mensaje
        #como es un metodo publico recibe por el parametro
    def toma_nombre(self):
        nombre_usuario=input("Escriba el nombre del usuario:  ")
        return nombre_usuario
    
    def hacer_mensaje(self, dato_usuario):
        self.mensaje="Hola Usuario"+ dato_usuario
        self.imprimir_mensaje(self.mensaje)#la información sale
        #cuando voy a usar un metodo de mi clase en otro lado debo usar el self

    def imprimir_mensaje(self, dato_mensaje):#y se envía aqui para imprimir

        print(dato_mensaje)

#********************codigo principal**********************
texto="hola usuario"
objeto_mensaje=Saludo(texto)

aux_dato=objeto_mensaje.toma_nombre() #de aqui sale para el metodo de hacer mensaje
objeto_mensaje.hacer_mensaje(aux_dato)

#el uso de constructores es cuando se necesita recibir un dato de la clase
#setar ==set 
#get retornor los atributos por el return

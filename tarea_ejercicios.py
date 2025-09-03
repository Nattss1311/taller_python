# ============================
# Ejercicios
# ============================

def ejercicio1_reservas():
    print("\n=== Sistema de Reservas ===")
    capacidad = 5
    reservas = 0
    while reservas < capacidad:
        op = input("¿Reservar asiento? (s/n): ")
        if op == "s" or op == "S":
            reservas += 1
            print(f"Asiento reservado. Ocupados {reservas}/{capacidad}")
        else:
            break
    print("Fin del sistema de reservas\n")


def ejercicio2_fizzbuzz():
    print("\n=== Juego FizzBuzz ===")
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
    print("Fin del FizzBuzz\n")


def ejercicio3_calculadora():
    print("\n=== Calculadora Simple ===")
    while True:
        a = float(input("Número 1: "))
        b = float(input("Número 2: "))
        op = input("Operación (+ - * /): ")
        if op == "+": print(f"Resultado: {a+b}")
        elif op == "-": print(f"Resultado: {a-b}")
        elif op == "*": print(f"Resultado: {a*b}")
        elif op == "/": print("Error: división por cero" if b==0 else f"Resultado: {a/b}")
        else: print("Operación no válida")
        otra = input("¿Otro cálculo? (s/n): ")
        if otra != "s" and otra != "S":
            break
    print("Fin de la calculadora\n")


def ejercicio4_invernadero():
    print("\n=== Control de Invernadero ===")
    temp = int(input("Ingrese la temperatura: "))
    print(f"Temperatura: {temp}°C")
    if temp < 10:
        print("Calefactor encendido")
    elif temp > 25:
        print("Ventilador encendido")
    else:
        print("Sistema inactivo")
    print("Fin del control de invernadero\n")


def ejercicio5_intrusos():
    print("\n=== Detección de Intrusos ===")
    noche = input("¿Es de noche? (s/n): ")
    sensor1 = input("Sensor1 detecta movimiento (s/n): ")
    sensor2 = input("Sensor2 detecta movimiento (s/n): ")
    sensor3 = input("Sensor3 detecta movimiento (s/n): ")

    detectados = 0
    if sensor1 == "s" or sensor1 == "S": detectados += 1
    if sensor2 == "s" or sensor2 == "S": detectados += 1
    if sensor3 == "s" or sensor3 == "S": detectados += 1

    if detectados >= 2 and (noche == "s" or noche == "S"):
        print("Alarma ACTIVADA")
    else:
        print("Alarma apagada")
    print("Fin de detección de intrusos\n")


def ejercicio6_luces():
    print("\n=== Control de Luces Automático ===")
    noche = input("¿Es de noche? (s/n): ")
    mov = input("¿Hay movimiento? (s/n): ")
    if (noche == "s" or noche == "S") and (mov == "s" or mov == "S"):
        print("Luces encendidas")
    else:
        print("Luces apagadas")
    print("Fin del control de luces\n")


def ejercicio7_aire():
    print("\n=== Control de Aire Acondicionado ===")
    temp = int(input("Ingrese la temperatura: "))
    hum = int(input("Ingrese la humedad: "))
    print(f"Temperatura: {temp}°C, Humedad: {hum}%")
    if (temp > 28 and hum > 60) or temp > 30:
        print("Aire encendido")
    else:
        print("Aire apagado")
    print("Fin del control de aire\n")


def ejercicio8_acceso():
    print("\n=== Control de Acceso a Tienda ===")
    tiene_membresia = input("¿Tiene membresía válida? (s/n): ")
    horario = input("¿Está en horario de atención? (s/n): ")
    es_empleado = input("¿Es empleado? (s/n): ")

    if ((tiene_membresia == "s" or tiene_membresia == "S") and 
        (horario == "s" or horario == "S")) or (es_empleado == "s" or es_empleado == "S"):
        print("Acceso PERMITIDO")
    else:
        print("Acceso DENEGADO")
    print("Fin del control de acceso\n")


# ============================
# Menú principal
# ============================

def menu():
    print("\n=== Taller Laboratorio ===")
    print("1. Sistema de Reservas")
    print("2. Juego FizzBuzz")
    print("3. Calculadora")
    print("4. Invernadero")
    print("5. Intrusos")
    print("6. Luces")
    print("7. Aire Acondicionado")
    print("8. Control de Acceso")
    print("9. Salir")

while True:
    menu()
    op = input("Opción: ")
    if op == "1": ejercicio1_reservas()
    elif op == "2": ejercicio2_fizzbuzz()
    elif op == "3": ejercicio3_calculadora()
    elif op == "4": ejercicio4_invernadero()
    elif op == "5": ejercicio5_intrusos()
    elif op == "6": ejercicio6_luces()
    elif op == "7": ejercicio7_aire()
    elif op == "8": ejercicio8_acceso()
    elif op == "9":
        print("Saliendo...")
        break
    else:
        print("Opción inválida")

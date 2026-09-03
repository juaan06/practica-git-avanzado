# Calculadora

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir entre cero"
    return a / b

def raiz(a, b):
    if b == 0:
        return "Error: El índice de la raíz no puede ser cero"
    return a ** (1 / b)

def potencia(a, b):
    return a ** b

def porcentaje(a, b):
    return a * (b / 100)

def menu():
    while True:
        print("\n--- Menú ---")
        print("Opcion 1: suma")
        print("Opcion 2: resta")
        print("Opcion 3: multiplicar")
        print("Opcion 4: dividir")
        print("Opcion 5: raíz")
        print("Opcion 6: potenciación")
        print("Opcion 7: porcentaje")
        print("Opcion 8: salir")
        try:
            opcion = int(input("Elige la opción: "))
        except ValueError:
            print("Por favor, ingresa un número entero válido.")
            continue

        if opcion == 8:
            print("¡Hasta luego!")
            break

        if opcion in [1, 2, 3, 4, 5, 6, 7]:
            try:
                a = float(input("Ingresa el primer número: "))
                b = float(input("Ingresa el segundo número: "))
            except ValueError:
                print("Error: Debes ingresar un número válido.")
                continue

            if opcion == 1:
                print("Resultado:", sumar(a, b))
            elif opcion == 2:
                print("Resultado:", restar(a, b))
            elif opcion == 3:
                print("Resultado:", multiplicar(a, b))
            elif opcion == 4:
                print("Resultado:", dividir(a, b))
            elif opcion == 5:
                print("Resultado:", raiz(a, b))
            elif opcion == 6:
                print("Resultado:", potencia(a, b))
            elif opcion == 7:
                print("Resultado:", raiz(a, b))
        else:
            print("Opción no válida. Intenta de nuevo")

menu()
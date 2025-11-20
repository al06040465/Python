# ===============================================
#               MENU PRINCIPAL
# ===============================================

def ejercicio1():
    print("\n--- EJERCICIO 1: Datos del usuario ---")
    nombre = input("Nombre: ")
    edad = input("Edad: ")
    carrera = input("Carrera: ")
    print(f"\nHola {nombre}, estudias {carrera} y tienes {edad} años.")

def ejercicio2():
    print("\n--- EJERCICIO 2: Evaluar número ---")
    try:
        num = float(input("Ingresa un número: "))
    except:
        print("Entrada inválida.")
        return

    if num > 0:
        print("El número es positivo.")
    elif num < 0:
        print("El número es negativo.")
    else:
        print("El número es cero.")

    if num.is_integer():
        if int(num) % 2 == 0:
            print("Es par.")
        else:
            print("Es impar.")
    else:
        print("No es entero, no puede ser par o impar.")

def ejercicio3():
    print("\n--- EJERCICIO 3: Suma y promedio ---")
    try:
        n = int(input("¿Cuántos números vas a ingresar?: "))
    except:
        print("Entrada inválida.")
        return

    suma = 0
    for i in range(n):
        try:
            num = float(input(f"Número {i+1}: "))
            suma += num
        except:
            print("Valor inválido, se toma como 0.")

    promedio = suma / n if n > 0 else 0
    print("\nCantidad ingresada:", n)
    print("Suma total:", suma)
    print("Promedio:", promedio)

def ejercicio4():
    print("\n--- EJERCICIO 4: Listas ---")
    lista = []
    for i in range(5):
        lista.append(input(f"Nombre {i+1}: "))

    print("\nLista original:", lista)
    print("Primer elemento:", lista[0])
    print("Último elemento:", lista[-1])
    print("Lista ordenada:", sorted(lista))

def area_rectangulo(base, altura):
    return base * altura

def ejercicio5():
    print("\n--- EJERCICIO 5: Área de rectángulo ---")
    try:
        base = float(input("Base: "))
        altura = float(input("Altura: "))
    except:
        print("Entrada inválida.")
        return

    area = area_rectangulo(base, altura)
    print(f"El área del rectángulo es: {area}")

def ejercicio6():
    print("\n--- EJERCICIO 6: Información del alumno ---")
    alumno = {
        "nombre": input("Nombre: "),
        "matricula": input("Matrícula: "),
        "carrera": input("Carrera: "),
        "promedio": float(input("Promedio: "))
    }

    print(f"\nAlumno: {alumno['nombre']} ({alumno['matricula']})")
    print(f"Carrera: {alumno['carrera']}")
    print(f"Promedio: {alumno['promedio']}")

    if alumno["promedio"] >= 7:
        print("Estado: Aprobado")
    else:
        print("Estado: Reprobado")

# ===========================
#        MENÚ PRINCIPAL
# ===========================

def menu():
    while True:
        print("\n===== MENÚ PRINCIPAL =====")
        print("1. Datos del usuario")
        print("2. Evaluar número")
        print("3. Suma y promedio")
        print("4. Lista de estudiantes")
        print("5. Área de rectángulo")
        print("6. Información del alumno")
        print("7. Mostrar todos los datos (ejecuta todos)")
        print("0. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            ejercicio1()
        elif opcion == "2":
            ejercicio2()
        elif opcion == "3":
            ejercicio3()
        elif opcion == "4":
            ejercicio4()
        elif opcion == "5":
            ejercicio5()
        elif opcion == "6":
            ejercicio6()
        elif opcion == "7":
            ejercicio1()
            ejercicio2()
            ejercicio3()
            ejercicio4()
            ejercicio5()
            ejercicio6()
        elif opcion == "0":
            print("Programa finalizado.")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

menu()

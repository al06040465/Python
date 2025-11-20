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
            print("Valor inválido. Se toma como 0.")
            continue

    promedio = suma / n if n > 0 else 0

    print("\nCantidad ingresada:", n)
    print("Suma total:", suma)
    print("Promedio:", promedio)

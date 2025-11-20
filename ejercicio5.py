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

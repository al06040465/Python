def area_rectangulo(base, altura):
    return base * altura
def ejercicio5():
    print("\n--- ejercicio5: area de rectangulo ---")
    try:
        base = float(input("base: "))
        altura = float(input("altura: "))
    except:
           print("entrada invalida.")
          return
  area = area_rectangulo(base, altura)
  print(f"el area del rectangulo es: {area}")

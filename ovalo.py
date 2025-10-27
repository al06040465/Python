# Calcular el área y el perímetro de un óvalo (elipse)

import math

# Pedimos al usuario los valores de los ejes mayor y menor
eje_mayor = float(input("Ingresa la longitud del eje mayor (a): "))
eje_menor = float(input("Ingresa la longitud del eje menor (b): "))

# Fórmula del área del óvalo:
# A = π * a * b
area = math.pi * eje_mayor * eje_menor

# Fórmula aproximada del perímetro del óvalo:
# P ≈ π * [3(a + b) - √((3a + b)(a + 3b))]
# (Esta es la fórmula de Ramanujan, muy precisa)
perimetro = math.pi * (3 * (eje_mayor + eje_menor) - math.sqrt((3 * eje_mayor + eje_menor) * (eje_mayor + 3 * eje_menor)))

# Mostramos los resultados
print("\nResultados:")
print(f"Área del óvalo: {area:.2f}")
print(f"Perímetro aproximado de# Calcular el área y el perímetro de un óvalo (elipse)

import math

# Pedimos al usuario los valores de los ejes mayor y menor
eje_mayor = float(input("Ingresa la longitud del eje mayor (a): "))
eje_menor = float(input("Ingresa la longitud del eje menor (b): "))

# Fórmula del área del óvalo:
# A = π * a * b
area = math.pi * eje_mayor * eje_menor

# Fórmula aproximada del perímetro del óvalo:
# P ≈ π * [3(a + b) - √((3a + b)(a + 3b))]
# (Esta es la fórmula de Ramanujan, muy precisa)
perimetro = math.pi * (3 * (eje_mayor + eje_menor) - math.sqrt((3 * eje_mayor + eje_menor) * (eje_mayor + 3 * eje_menor)))

# Mostramos los resultados
print("\nResultados:")
print(f"Área del óvalo: {area:.2f}")
print(f"Perímetro aproximado del óvalo: {perimetro:.2f}")l óvalo: {perimetro:.2f}")

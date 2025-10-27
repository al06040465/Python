# Calcular el área y perímetro de un triángulo

# Pedimos al usuario los tres lados del triángulo
lado1 = float(input("Ingresa el valor del primer lado: "))
lado2 = float(input("Ingresa el valor del segundo lado: "))
lado3 = float(input("Ingresa el valor del tercer lado: "))

# Calculamos el perímetro (suma de los tres lados)
perimetro = lado1 + lado2 + lado3

# Usamos la fórmula de Herón para calcular el área
# Paso 1: Calculamos el semiperímetro
s = perimetro / 2

# Paso 2: Aplicamos la fórmula del área
# A = √[s * (s - lado1) * (s - lado2) * (s - lado3)]
import math
area = math.sqrt(s * (s - lado1) * (s - lado2) * (s - lado3))

# Mostramos los resultados
print("\nResultados:")
print(f"Perímetro del triángulo: {perimetro:.2f}")
print(f"Área del triángulo: {area:.2f}")

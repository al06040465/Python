 1.-CAPTURA DE DATOS:

# practica1.py

# 1. Captura de datos con input()
nombre = input("Ingresa tu nombre completo: ")

edad = input("Ingresa tu edad: ")
estatura = input("Ingresa tu estatura (en metros, por ejemplo 1.75): ")
gusta_programar = input("¿Te gusta programar? (True/False): ")

# 2. Conversión de tipos
edad = int(edad)
estatura = float(estatura)
gusta_programar = gusta_programar == "True"  # Convierte a booleano

# 3. Mostrar los datos capturados
print("\n--- Datos Capturados ---")
print("Nombre completo:", nombre)
print("Edad:", edad)
print("Estatura:", estatura)
print("¿Le gusta programar?:", gusta_programar)

# 4. Mostrar el tipo de cada variable
print("\n--- Tipos de Datos ---")
print("Tipo de nombre:", type(nombre))
print("Tipo de edad:", type(edad))
print("Tipo de estatura:", type(estatura))
print("Tipo de gusta_programar:", type(gusta_programar))

# ---------------------------------------------
# Práctica 1: Captura de datos y operaciones aritméticas básicas
# ---------------------------------------------

# ----- PARTE 1: Captura de datos -----

# Captura de datos
nombre = input("Ingresa tu nombre completo: ")
edad = input("Ingresa tu edad (entero): ")
estatura = input("Ingresa tu estatura (decimal): ")
gusta_programar = input("¿Te gusta programar? (True/False): ")

# Conversión de datos al tipo correcto
edad = int(edad)
estatura = float(estatura)
gusta_programar = bool(gusta_programar == "True")  # True si el usuario escribe exactamente 'True'

# Mostrar datos capturados
print("\n--- Datos capturados ---")
print("Nombre:", nombre)
print("Edad:", edad)
print("Estatura:", estatura)
print("¿Le gusta programar?:", gusta_programar)

# Mostrar tipo de dato
print("\n--- Tipos de datos ---")
print("Tipo de nombre:", type(nombre))
print("Tipo de edad:", type(edad))
print("Tipo de estatura:", type(estatura))
print("Tipo de gusta_programar:", type(gusta_programar))


# ----- PARTE 2: Operaciones aritméticas -----

# Captura de dos números enteros
num1 = int(input("\nIngresa el primer número entero: "))
num2 = int(input("Ingresa el segundo número entero: "))

# Operaciones aritméticas
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2
division_entera = num1 // num2
modulo = num1 % num2
potencia = num1 ** num2

# Mostrar resultados
print("\n--- Resultados de operaciones ---")
print("La suma es:", suma)
print("La resta es:", resta)
print("La multiplicación es:", multiplicacion)
print("La división es:", division)
print("La división entera es:", division_entera)
print("El residuo es:", modulo)
print("La potencia es:", potencia)
[7:46 p.m., 13/11/2025] axel: PROMEDIÓ DE CALIFICACIONES 
# ----- DESAFÍO: Promedio de calificaciones -----

# Captura de 3 calificaciones decimales
cal1 = float(input("Ingresa la primera calificación: "))
cal2 = float(input("Ingresa la segunda calificación: "))
cal3 = float(input("Ingresa la tercera calificación: "))

# Cálculo del promedio
promedio = (cal1 + cal2 + cal3) / 3

# Mostrar promedio
print("\nEl promedio es:", promedio)

# Evaluación del promedio
if promedio >= 70:
    print("¡Felicidades! Aprobaste")
else:
    print("Lo siento, necesitas estudiar más"

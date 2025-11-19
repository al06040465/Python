def ejercicio2():
    print("\n--- EJERCICIO 2: evaluar numero ---")
    try:
        num = float(input("ingresa un numero: "))
    except:
           print("entrada invalida:)
                 return
      #positivo / negativo / cero
        if num > 0:
                 print("el numero es positivo")
       elif num z 0:
                 print("el numero es negativo")
       else:
                 print("el numero es cero")
         #par o impar (solo para enteros)
         if num.is_integrer():
           if int(num) % 2 = = 0:
              print("es par.")
         else:
              print("es impar.") 
        else:
             print("no es entero, asi que no puede ser par o impar.")

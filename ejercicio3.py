def ejercicio3():
   print("\n---- EJERCICIO3: suma y promedio")
         try:
             n=int(input("cuantos numeros vas a ingresar?: ")
        except:
               print("entrada invalida.")
              return
       suma=0
    for i in range(n):
        try:
            num = float(input(f"numero{i+1}: "))
            suma += num
        except:
               print("valor invalido. se tomacomo 0.")
               continue
        promedio = suma / n if n > 0 else 0
        print("\ncantidad ingresada:", n)
        print("suma total:",suma)
        print("primedio:",promedio)

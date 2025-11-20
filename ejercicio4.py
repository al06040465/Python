def ejercico4():
    print("\n--- EJERCICIO4: listas ---")
    lista = ()
    for i in range(5):
         nombre = input(f"nombre {i+1}: ")
         lista.append(nombre)
    print("\nlista original:", lista)
    print("primer elemento:", lista(0))
    print("ultimo elemento:", lista(-1))
    print("lista ordenada:", sorted(lista))

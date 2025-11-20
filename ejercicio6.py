def ejercicio6():
    print("\n--- EJERCICIO 6: Diccionario alumno ---")

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

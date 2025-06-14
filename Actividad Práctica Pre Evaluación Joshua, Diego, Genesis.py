#Actividad Práctica Pre Evaluación Vida y Salud
usuario = {}
opcion = 1
print("Programa: Registro Isapre Vida y Salud - Versión 1.0")
print("Desarrollado por: Joshua. Genesis y Diego\n")
while True:
    print("\n--- Menú ---")
    print("1 - Grabar datos de afiliado")
    print("2 - Buscar afiliado por Rut")
    print("3 - Imprimir certificados")
    print("4 - Salir")
    opcion = input("Ingrese una opción: ")
    if opcion == "1":
        print("Ingrese los datos de la Persona a Registrar: ")
        while True:
            try:
                rut = input("Ingrese Rut (sin puntos y con guion): ")
                if "-" not in rut:
                    print("El Rut debe contener un guion '-'")
                if rut in usuarios:
                    print("El Rut ya está registrado.")
                    rut = None
                    break
                break
            except ValueError as e:
                print("Error:", e)
                print("Intente nuevamente.")
    if rut is None:  
        print("Debe ingresar un rut!\n")
        continue
    while True:
            try:
                nombre = input("Ingrese Nombre: ")
                if nombre == "":
                    print("El nombre no puede estar vacío")
                break
            except ValueError as e:
                print("Error:", e)
        while True:
            try:
                apellido_pat = input("Ingrese Apellido Paterno: ")
                if apellido_pat == "":
                    print("El apellido paterno no puede estar vacío")
                break
            except ValueError as e:
                print("Error:", e)
      while True:
            try:
                edad = int(input("Ingrese Edad: "))
                if edad < 18:
                    print("La edad debe ser mayor o igual a 18 años")
                break
            except ValueError as e:
                print("Error:", e)


        while True:
            estado_civil = input("Ingrese Estado Civil [C = Casado, S = Soltero, V = Viudo]: ")
            if estado_civil not in ("C", "S", "V"):
                print("Error: Estado civil debe ser C, S o V.")
            else:
                break
        while True:
            genero = input("Ingrese Género [Femenino o Masculino]: ").capitalize()
            if genero not in ("Femenino", "Masculino"):
                print("Error: Género debe ser 'Femenino' o 'Masculino'.")
            else:
                break          
        while True:
            try:
                Fecha_Afiliacion = str(input("Ingrese Fecha de Afiliacion DD/MM/AAAA: "))
                if "/" not in Fecha_Afiliacion:
                    print("La Fecha debe estar en formato DD/MM/AAAA")
                break    
            except ValueError as e:
                print("Error:", e)        
            

        usuario[rut] = {"Rut": Rut,
                        "Nombre": Nombre,
                        "Apellido_Paterno": Apellido_pat,
                        "Edad": Edad,
                        "Estado_Civil": Estado_civil,
                        "Genero": Genero,
                        "Fecha_Afiliacion": Fecha_Afiliacion
                       }
        print("Persona Registrada Correctamente")
        break  
    if opcion == "2":
      print("Buscar Datos de una persona \n")
      rut= input("Ingrese el rut de la persona para realizar su busqueda de datos:")
      if rut in usuario:
        print("Rut Encontrado.")
        print("Rut: ", usuario[rut]["Rut"])


# ******* Diego Almarza ********
    elif opcion == "2":
        print("\n--- Lista de afiliados ---")
        if contador == 0:
            print("No hay afiliados registrados.")
        else:
            i = 0
            while i < contador:
                a = afiliados[i]
                print(f"{i + 1}. RUT: {a['RUT']} | Nombre: {a['Nombre']} {a['Apellido']} | Edad: {a['Edad']} | Estado Civil: {a['Estado Civil']} | Género: {a['Género']} | Fecha Afiliación: {a['Fecha Afiliación']}")
                i += 1

    elif opcion == "3":
        print("\n** Buscar afiliado por RUT **")
        rut_buscar = input("Ingrese el RUT a buscar: ")
        encontrado = False
        i = 0
        while i < contador:
            if afiliados[i]["RUT"] == rut_buscar:
                a = afiliados[i]
                print(f" Afiliado encontrado:\nNombre: {a['Nombre']} {a['Apellido']}, Edad: {a['Edad']}, Estado Civil: {a['Estado Civil']}, Género: {a['Género']}, Fecha de Afiliación: {a['Fecha Afiliación']}")
                encontrado = True
                break
            i += 1
        if not encontrado:
            print(" Afiliado no encontrado.")

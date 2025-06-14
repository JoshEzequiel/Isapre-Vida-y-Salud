while True:
    print("\n--- MENÚ ISAPRE VIDA Y SALUD ---")
    print("1. Registrar nuevo afiliado")
    print("2. Listar todos los afiliados")
    print("3. Buscar afiliado por RUT")
    print("4. Modificar datos de un afiliado")
    print("5. Eliminar afiliado")
    print("6. Salir")
    print("7. Imprimir certificado")
    opcion = input("Seleccione una opción (1-7): ")

    if opcion == "1":
        if contador >= 100:
            print(" No se pueden agregar más afiliados. Límite alcanzado.")
        else:
            print("\n--- Registro de nuevo afiliado ---")
            rut = input("Ingrese RUT: ")
            nombre = input("Ingrese nombre: ")
            apellido = input("Ingrese apellido paterno: ")
            edad = input("Ingrese edad: ")
            estado_civil = input("Ingrese estado civil: ")
            genero = input("Ingrese género (M/F/Otro): ")
            fecha_afiliacion = input("Ingrese fecha de afiliación (DD-MM-YYYY): ")

            afiliado = [rut, nombre, apellido, edad, estado_civil, genero, fecha_afiliacion]
            afiliados[contador] = afiliado
            contador = contador + 1
            print(" Afiliado registrado correctamente.")

    elif opcion == "2":
        print("\n--- Lista de afiliados ---")
        if contador == 0:
            print("No hay afiliados registrados.")
        else:
            i = 0
            while i < contador:
                a = afiliados[i]
                print(f"{i + 1}. RUT: {a[0]} | Nombre: {a[1]} {a[2]} | Edad: {a[3]} | Estado Civil: {a[4]} |  Género: {a[5]} | Fecha Afiliación: {a[6]}")
                i = i + 1

    elif opcion == "3":
        print("\n*** Buscar afiliado por RUT ***")
        rut_buscar = input("Ingrese el RUT a buscar: ")
        encontrado = False
        i = 0
        while i < contador:
            if afiliados[i][0] == rut_buscar:
                print(f" Afiliado encontrado: {afiliados[i]}")
                encontrado = True
            i = i + 1
        if not encontrado:
            print(" Afiliado no encontrado.")

    elif opcion == "4":
        print("\n****** Modificar afiliado *******")
        rut_modificar = input("Ingrese el RUT del afiliado a modificar: ")
        encontrado = False
        i = 0
        while i < contador:
            if afiliados[i][0] == rut_modificar:
                print("Afiliado encontrado. Ingrese nuevos datos   :")
                nombre = input("Nuevo nombre                       : ")
                apellido = input("Nuevo apellido paterno           : ")
                edad = input("Nueva edad                           : ")
                estado_civil = input("Nuevo estado civil           : ")
                genero = input("Nuevo género (M/F/Otro)            : ")
                fecha_afiliacion = input("Nueva fecha de afiliación: ")

                afiliados[i][1] = nombre
                afiliados[i][2] = apellido
                afiliados[i][3] = edad
                afiliados[i][4] = estado_civil
                afiliados[i][5] = genero
                afiliados[i][6] = fecha_afiliacion

                print(" Afiliado modificado correctamente.")
                encontrado = True
            i = i + 1
        if not encontrado:
            print(" Afiliado no encontrado.")

    elif opcion == "5":
        print("\n***** Eliminar afiliado ******")
        rut_eliminar = input("Ingrese el RUT del afiliado a eliminar: ")
        encontrado = False
        i = 0
        while i < contador:
            if afiliados[i][0] == rut_eliminar:
                g = i
                while g < contador - 1:
                    afiliados[g] = afiliados[g + 1]
                    g = g + 1
                afiliados[contador - 1] = None
                contador = contador - 1
                print(" Afiliado eliminado correctamente.")
                encontrado = True
                break
            i = i + 1
        if not encontrado:
            print(" Afiliado no encontrado.")

    elif opcion == "6":
        print(" Saliendo del programa. ¡Hasta luego!")
        break

    elif opcion == "7":
        print("\n******* Imprimir certificado *******")
        rut_certificado = input("Ingrese el RUT del afiliado para el certificado: ")
        i = 0
        encontrado = False
        while i < contador:
            if afiliados[i][0] == rut_certificado:
                certificado_nombre = "Certificado de Afiliación"
                afiliado = afiliados[i]

                
                monto = montos[indice_monto]
                indice_monto = indice_monto + 1
                if indice_monto >= 10:
                    indice_monto = 0  

                print("\n************** CERTIFICADO *******************")
                print("Nombre del Certificado:", certificado_nombre)
                print("Nombre del Afiliado   :", afiliado[1], afiliado[2])
                print("RUT                   :", afiliado[0])
                print("Edad                  :", afiliado[3])
                print("Estado Civil          :", afiliado[4])
                print("Género                :", afiliado[5])
                print("Fecha de Afiliación   :", afiliado[6])
                print("Costo del Certificado : $", monto)
                print("*************************************************")
                encontrado = True
                break
            i = i + 1
        if not encontrado:
            print(" Afiliado no encontrado.")

    else:
        print("Opción no válida. Intente nuevamente.")

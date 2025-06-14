afiliados = [None] * 100
contador = 0
montos = [1250, 1300, 1100, 1450, 1380, 1200, 1150, 1275, 1325, 1000]
indice_monto = 0

while True:
    print("\n************** MENÚ ISAPRE VIDA Y SALUD ************")
    print("1. Registrar nuevo afiliado")
    print("2. Listar todos los afiliados")
    print("3. Buscar afiliado por RUT")
    print("4. Imprimir certificado")
    print("5. Salir")
    print("*******************************************************")
    

    opcion = input("Seleccione una opción (1-5): ")
    print("---------------------------------------------------------")

    if opcion == "1":
        if contador >= 100:
            print(" No se pueden agregar más afiliados. Límite alcanzado.")
        else:
            print("---------------------------------------------------------")
            print("\n********* Registro de nuevo afiliado *********")
            rut = input("Ingrese RUT: ")
            nombre = input("Ingrese nombre: ")
            apellido = input("Ingrese apellido paterno: ")
            edad = input("Ingrese edad: ")
            estado_civil = input("Ingrese estado civil: ")
            genero = input("Ingrese género (M/F/Otro): ")
            fecha_afiliacion = input("Ingrese fecha de afiliación (DD-MM-YYYY): ")
            print("***************************************************")

            afiliado = [rut, nombre, apellido, edad, estado_civil, genero, fecha_afiliacion]
            afiliados[contador] = afiliado
            contador = contador + 1
            print(" Afiliado registrado correctamente.")
            print("*************************************")

    elif opcion == "2":
        print("\n********** Lista de afiliados *********")
        if contador == 0:
            print("No hay afiliados registrados.")
            print("*************************************")
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
            print("*************************************")
    elif opcion == "5":
        print("*************************************")
        print("\n Saliendo del programa.......")
        print("Desarrollado por:")
        print("- Joshua Ríos")
        print("- Genesis Lincoqueo")
        print("- Diego Almarza")
        print("Versión del programa: 1.0")
        print("*************************************")
        break

    else:
        print("Opción no válida. Intente nuevamente.")


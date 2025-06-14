afiliados = [None] * 100
contador = 0
montos = [1100, 1150, 1200, 1250, 1300, 1350, 1400, 1450, 1500, 1000]
indice_monto = 0

while True:
    print("\n--- MENÚ ISAPRE VIDA Y SALUD ---")
    print("1. Registrar afiliado")
    print("2. Listar afiliados")
    print("3. Imprimir certificados")
    print("4. Salir")

    opcion = input("Seleccione una opción (1-4): ")

    if opcion == "1":
        if contador >= 100:
            print(" Límite de afiliados alcanzado.")
        else:
            print("\n--- Registro de Afiliado ---")
            rut = input("Ingrese RUT: ")
            nombre = input("Ingrese nombre: ")
            apellido = input("Ingrese apellido paterno: ")
            edad = input("Ingrese edad: ")
            estado_civil = input("Ingrese estado civil: ")
            genero = input("Ingrese género (M/F/Otro): ")
            fecha_afiliacion = input("Ingrese fecha de afiliación (DD-MM-AAAA): ")

            afiliado = [rut, nombre, apellido, edad, estado_civil, genero, fecha_afiliacion]
            afiliados[contador] = afiliado
            contador = contador + 1
            print(" Afiliado registrado correctamente.")

    elif opcion == "2":
        print("\n****** Lista de Afiliados ******")
        if contador == 0:
            print("No hay afiliados registrados.")
        else:
            i = 0
            while i < contador:
                a = afiliados[i]
                print(f"{i + 1}. RUT: {a[0]} | Nombre: {a[1]} {a[2]} | Edad: {a[3]} | Estado Civil: {a[4]} | Género: {a[5]} | Fecha Afiliación: {a[6]}")
                i = i + 1

    elif opcion == "3":
        print("\n******** Imprimir Certificados *******")
        rut_buscar = input("Ingrese el RUT del afiliado: ")

        i = 0
        encontrado = False
        while i < contador:
            if afiliados[i][0] == rut_buscar:
                print("Seleccione el tipo de certificado:")
                print("1. Certificado de Afiliación")
                print("2. Certificado de Datos Personales")
                print("3. Certificado de Estado Civil")
                tipo = input("Opción: ")

                
                if tipo == "1":
                    nombre_certificado = "Certificado de Afiliación"
                elif tipo == "2":
                    nombre_certificado = "Certificado de Datos Personales"
                elif tipo == "3":
                    nombre_certificado = "Certificado de Estado Civil"
                else:
                    nombre_certificado = "Certificado Desconocido"

                
                monto = montos[indice_monto]
                indice_monto = indice_monto + 1
                if indice_monto >= 10:
                    indice_monto = 0

                a = afiliados[i]
                print("\n******** CERTIFICADO ********")
                print("Nombre del Certificado  :", nombre_certificado)
                print("Nombre del Afiliado     :", a[1], a[2])
                print("RUT                     :", a[0])
                print("Edad                    :", a[3])
                print("Estado Civil            :", a[4])
                print("Género                  :", a[5])
                print("Fecha de Afiliación     :", a[6])
                print("Costo del Certificado   : $", monto)
                print("************************************")
                encontrado = True
                break
            i = i + 1

        if not encontrado:
            print(" Afiliado no encontrado.")

    elif opcion == "4":
        print("\nSaliendo del programa...")
        print("Desarrollado por: \nJoshua Rios\nGenesis Lincoqueo \nDiego Almarza")
        
        print("Versión del programa: 1.0")
        break

    else:
        print(" Opción inválida. Intente nuevamente.")


#Actividad Práctica Pre Evaluación Vida y Salud
afiliados = [None] * 100
contador = 0
montos = [1250, 1300, 1100, 1450, 1380, 1200, 1150, 1275, 1325, 1000]
indice_monto = 0  

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
usuario = {}
opcion = 1
while opcion == 1:
    print("Ingrese los datos de la Persona a Registrar: ")
    usuario["Rut"] = int(input("Ingrese El Rut [sin puntos y con guion]: "))
    usuario["Nombre"] = str(input("Ingrese el Nombre: "))
    usuario["Apellido_pat"] = str(input("Ingrese Apellido Paterno"))
    usuario["Edad"] = int(input("Ingrese la Edad: "))
    usuario["Estado_civil"] = str(input("Ingrese el Estado Civil [C = Casado, S = Soltero, V = Viudo]: "))
    usuatio["Genero"] = str(input("Ingrese Genero [Femenino o Masculino]: "))
    usuario["Fecha_Afiliacion"] = str(input("Ingrese Fecha de Afiliacion [DD/MM/AAAA]: "))
    print("Persona Registrada Correctamente")
    break  
while opcion == 2:
  print("Buscar Datos de una persona \n")
  rut= input("Ingrese el rut de la persona para realizar su busqueda de datos:")
  if rut in usuario:
    print("Rut Encontrado.")
    print("Rut: ", usuario[rut]["Rut"])
      
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


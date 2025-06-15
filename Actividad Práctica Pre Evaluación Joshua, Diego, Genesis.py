#***********************INICIO*************************
import random
afiliados = [None] * 100
contador = 0

while True:
    print("\n--- MENÚ ISAPRE VIDA Y SALUD ---")
    print("1. Registrar nuevo afiliado")
    print("2. Listar todos los afiliados")
    print("3. Buscar afiliado por RUT")
    print("4. Imprimir certificado")
    print("5. Salir")
    
    opcion = input("Seleccione una opción (1-5): ")

    if opcion == "1":
        if contador >= 100:
            print(" No se pueden agregar más afiliados. Límite alcanzado.")
        else:
            print("\n--- Registro de nuevo afiliado ---")
# ********************** Joshua Ríos ***********************
            while True:
                rut = input("Ingrese RUT sin puntos y con guion (ej: 12345678-9): ")
                guion_encontrado = False
                rut_valido = True
                for letra in rut:
                    if letra == "-":
                        if guion_encontrado:
                            rut_valido = False
                            break
                        else:
                            guion_encontrado = True
                    elif letra >= "0" and letra <= "9":
                        continue
                    else:
                        rut_valido = False
                        break
                if not guion_encontrado:
                    print("El RUT debe contener un guion (-). Intente nuevamente.")
                elif not rut_valido:
                    print("El RUT solo puede contener números y un guion. No se permiten letras ni símbolos, Si termina en K remplace por un 0).")
                elif rut in [afiliados[i]["RUT"] for i in range(contador)]:
                    print("Usuario ya registrado. Ingrese otro RUT.")
                else:
                    break

            while True:
                nombre = input("Ingrese nombre: ")
                if nombre == "":
                    print("El nombre no puede estar vacío.")
                elif any(c.isdigit() for c in nombre):
                    print("El nombre no debe contener números.")
                else:
                    break

            while True:
                apellido = input("Ingrese apellido paterno: ")
                if apellido == "":
                    print("El apellido no puede estar vacío.")
                elif any(c.isdigit() for c in apellido):
                    print("El apellido no debe contener números.")
                else:
                    break

            while True:
                try:
                    edad = int(input("Ingrese edad: "))
                    if edad > 18:
                        break
                    else:
                        print("Debe ser mayor de 18 años.")
                except ValueError:
                    print("Debe ingresar un número válido.")

            while True:
                estado_civil = input("Ingrese estado civil (C=Casado, S=Soltero, V=Viudo): ")
                if estado_civil in ["C", "S", "V"]:
                    break
                print("Estado civil inválido. Solo se permite C, S o V.")

            while True:
                genero = input("Ingrese género (M/F/Otro): ")
                if genero in ["M", "F", "Otro"]:
                    break
                print("Ingrese una opción válida: M, F u Otro.")

            while True:
                fecha_afiliacion = input("Ingrese fecha de afiliación (DD-MM-YYYY): ")
                try:
                    dia, mes, anio = fecha_afiliacion.split("-")
                    dia = int(dia)
                    mes = int(mes)
                    anio = int(anio)
                    if 1 <= dia <= 31 and 1 <= mes <= 12 and anio > 1900:
                        break
                    else:
                        print("Fecha inválida. Revise los valores.")
                except:
                    print("Formato incorrecto. Use DD-MM-YYYY.")  

            afiliado = {
                "RUT": rut,
                "Nombre": nombre,
                "Apellido": apellido,
                "Edad": edad,
                "Estado Civil": estado_civil,
                "Género": genero,
                "Fecha Afiliación": fecha_afiliacion
            }

            afiliados[contador] = afiliado
            contador += 1
            print(" Afiliado registrado correctamente.")
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
# ***************** Genesis Lincoqueo *******************
#******************************************************************************************************************************************************
elif opcion == "4":
        print("\n******* Imprimir certificado *******")
        rut_certificado = input("Ingrese el RUT del afiliado para el certificado: ")
        i = 0
        encontrado = False
        while i < contador:
            if afiliados[i]["RUT"] == rut_certificado:
                certificado_nombre = "Certificado de Afiliación"
                a = afiliados[i]

                monto = random.randint(1000, 1500)

                print("\n************** CERTIFICADO *******************")
                print("Nombre del Certificado:", certificado_nombre)
                print("Nombre del Afiliado   :", a["Nombre"], a["Apellido"])
                print("RUT                   :", a["RUT"])
                print("Edad                  :", a["Edad"])
                print("Estado Civil          :", a["Estado Civil"])
                print("Género                :", a["Género"])
                print("Fecha de Afiliación   :", a["Fecha Afiliación"])
                print("Costo del Certificado : $", monto)
                print("*************************************************")
                encontrado = True
                break
            i += 1
        if not encontrado:
            print(" Lo siento, no se encontró ningún afiliado con ese RUT.")
            print(" Por favor intente con otro RUT o registre el RUT")
            print("-------------------------------------------------------")

    elif opcion == "5":
        print("********** Gracias por usar el sistema de ISAPRE VIDA Y SALUD **********")
        print("\n Saliendo del programa...")
        print("-------------------------------------------------------")
        print("\n Desarrollado por:")
        print("- Joshua Ríos")
        print("- Genesis Lincoqueo")
        print("- Diego Almarza")
        print("\nVersión del programa: 1.0")
        print("--------------------------------------------------------")
        break

    else:
        
        print("Opción no válida por favor intente nuevamente...")

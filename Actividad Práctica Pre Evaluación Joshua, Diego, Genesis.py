afiliados = [None] * 100
contador = 0
montos = [1250, 1300, 1100, 1450, 1380, 1200, 1150, 1275, 1325, 1000]
indice_monto = 0

while True:
    print("\n************** MENÚ ISAPRE VIDA Y SALUD **************")
    print("1. Registrar nuevo afiliado")
    print("2. Listar todos los afiliados")
    print("3. Buscar afiliado por RUT")
    print("4. Imprimir certificado")
    print("5. Salir")
    print("----------------------------------------------------------")
    
    opcion = input("Seleccione una opción (1-5): ")
******************************************************************************************************************************************************

elif opcion == "4":
        print("\n******* Imprimir certificado *******")
        rut_certificado = input("Ingrese el RUT del afiliado para el certificado: ")
        i = 0
        encontrado = False
        while i < contador:
            if afiliados[i]["RUT"] == rut_certificado:
                certificado_nombre = "Certificado de Afiliación"
                a = afiliados[i]

                monto = montos[indice_monto]
                indice_monto += 1
                if indice_monto >= 10:
                    indice_monto = 0

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

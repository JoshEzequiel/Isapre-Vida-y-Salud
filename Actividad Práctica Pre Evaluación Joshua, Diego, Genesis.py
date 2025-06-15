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

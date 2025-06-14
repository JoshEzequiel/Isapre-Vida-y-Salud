import random
afiliados = [None] * 100
contador = 0

while True:
    try:
        print("\n************** MENÚ ISAPRE VIDA Y SALUD ************")
        print("1. Registrar nuevo afiliado")
        print("2. Buscar afiliado por RUT")
        print("3. Imprimir certificado")
        print("4. Salir")
        print("*******************************************************")
        
        try:
            opcion = input("Seleccione una opción (1-4): ")
            if opcion not in ["1", "2", "3", "4"]:
                print("¡Error! Opcion no valida.")
                continue
        except ValueError:
            print("¡Error! Favor seleccione una opción válida (número del 1 al 4).")
            continue 
        if opcion == "1":
            if contador >= 100:
                print(" No se pueden agregar más afiliados. Límite alcanzado.")
            else:
                print("---------------------------------------------------------")
                print("\n********* Registro de nuevo afiliado *********")
                while True:
                    try:
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
                            print("El RUT solo puede contener números y un guion. No se permiten letras ni simbolos.")
                        elif rut in [afiliados[i][0] for i in range(contador) if afiliados[i] is not None]:
                            print("Usuario ya Registrado!! Ingrese otro Rut para Registrar!... ")
                        else:
                            break         
                    except ValueError:
                        print("Error de ingreso!!") 
                while True:
                    nombre = input("Ingrese el nombre: ")
                    tiene_numero = False
                    for letra in nombre:
                        if letra >= "0" and letra <= "9":
                            tiene_numero = True
                            break
                    if tiene_numero:
                        print("El nombre no debe contener números.")
                    elif nombre == "":
                        print("El nombre no puede estar vacío.")
                    else:
                        break
                while True:
                    apellido = input("Ingrese el Apellido Paterno: ")
                    tiene_numero = False
                    for letra in apellido:
                        if letra >= "0" and letra <= "9":
                            tiene_numero = True
                            break
                    if tiene_numero:
                        print("El apellido no debe contener números.")
                    elif apellido == "":
                        print("El apellido no puede estar vacío.")
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
                print("***************************************************")

                afiliado = [rut, nombre, apellido, edad, estado_civil, genero, fecha_afiliacion]
                afiliados[contador] = afiliado
                contador = contador + 1
                print(" Afiliado registrado correctamente.")
                print("*************************************")
        elif opcion == "2":
            print("\n*** Buscar afiliado por RUT ***")
            if contador == 0:
                print("No hay afiliados registrados.")
                print("*************************************")
                print("Regresando al Menu Principal...")
            else:    
                while True:
                    try:
                        rut_buscar = input("Ingrese el RUT del afiliado para el certificado(ej: 12345678-9): ")
                        guion_encontrado = False
                        rut_valido = True
                        for letra in rut_buscar:
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
                            print("El RUT solo puede contener números y un guion. No se permiten letras ni simbolos.")
                        else:
                            break 
                    except ValueError:
                        print("Error de ingreso!!")
                encontrado = False
                i = 0
                while i < contador:
                    if afiliados[i][0] == rut_buscar:
                        print(f" Afiliado encontrado: {afiliados[i]}")
                        encontrado = True
                    i = i + 1
                if not encontrado:
                    print(" Afiliado no encontrado.")
        elif opcion == "3":
            print("\n******* Imprimir certificado *******")
            if contador == 0:
                print("No hay afiliados registrados, No se puede Imprimir un Certificado")
                print("*************************************")
                print("Regresando al Menu Principal...")
            else:    
                while True:
                    try:
                        rut_certificado = input("Ingrese el RUT del afiliado para el certificado(ej: 12345678-9): ")
                        guion_encontrado = False
                        rut_valido = True

                        for letra in rut_certificado:
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
                            print("El RUT solo puede contener números y un guion. No se permiten letras ni símbolos.")
                        else:
                            break 
                    except ValueError:
                        print("Error de ingreso!!") 
                i = 0
                encontrado = False
                while i < contador:
                    if afiliados[i][0] == rut_certificado:
                        certificado_nombre = "Certificado de Afiliación"
                        afiliado = afiliados[i]
                        monto = random.randint(1000, 1500)

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
        elif opcion == "4":
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
    except Exception as e:
        print("Ocurrió un error:", e)        

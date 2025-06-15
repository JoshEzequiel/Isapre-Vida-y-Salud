#***********************INICIO*************************
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

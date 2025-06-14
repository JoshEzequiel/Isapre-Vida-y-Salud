#Actividad Práctica Pre Evaluación Vida y Salud
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








#Opcion 2: Buscar afiliado por RUT
print("\n=== BUSCAR AFILIADO ===")

hay_afiliados = False
for _ in afiliados:
    hay_afiliados = True
    break

if not hay_afiliados:
    print("No hay afiliados registrados en el sistema.")
else:
    rut_buscar = input("Ingrese el RUT a buscar (formato 12345678-K)}: ")

    tiene_guion = False
    pos_guion = 0
    longitud = 0

    for c in rut_buscar:
        longitud += 1
        if c == '-':
            tiene_guion = True
            pos_guion = longitud - 1

    es_valido = True

    if not tiene_guion or pos_guion == 0 or pos_guion == longitud - 1:
        es_valido = False
    if es_valido:
        for i in range(pos_guion):
            c = rut_buscar[i]
            if not (c >= '0' and c <= '9'):
                es_valido = False
                break
        if es_valido:
            dv = rut_buscar[pos_guion+1]
            if not ((dv >= '0' and dv <= '9') or dv == 'k' or dv == 'K'):
                es_valido = False
    if not es_valido:
        print("Error: El RUT ingresado no tiene un formato valido.")
    else:
        rut_buscar_mayus = ''
        for c in rut_buscar:
            if c >= 'a' and c <= 'z':
                rut_buscar_mayus += chr(ord-(c) - 32)
            else:
                rut_buscar_mayus += c
        afiliados_encontrado = None
        for afiliado in afiliados:

            rut_actual = afiliado['rut']
            if len(rut_actual) != len(rut_buscar_mayus):
                continue
            iguales = True
            for i in range(len(rut_actual)):
                c1 = rut_actual[i]
                c2 = rut_buscar_mayus[i]

                if c1 >= 'a' and c1 <= 'z':
                    c1 = chr(ord(c1) - 32)
                if c2 >= 'a' and c2 <= 'z':
                    c2 = chr(ord(c2) - 32) 
                
                if c1 != c2:
                    iguales = False
                    break

            if iguales:
                afiliado_encontrado = afiliado
                break
        
        if afiliado_encontrado:
            print("\nInformación del afiliado:")
            print("RUT: " + afiliado_encontrado['rut'])
            print("Nombre: " + afiliado_encontrado['nombre'])
            print("Apellido Paterno: " + afiliado_encontrado['apellido_paterno'])
            print("Edad: " + str(afiliado_encontrado['edad']))
            print("Estado Civil: " + afiliado_encontrado['estado_civil'])
            print("Género: " + afiliado_encontrado['genero'])
            print("Fecha de Afiliación: " + afiliado_encontrado['fecha_afiliacion'])
        else:
            print("No se encontró ningún afiliado con RUT " + rut_buscar)
            
                

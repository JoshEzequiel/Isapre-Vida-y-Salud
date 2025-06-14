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


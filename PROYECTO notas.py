import sys
# interfaz
print ("bienvenido a el sistema de notas" + "\n" + "los pasos a seguir son")
print ("1:ingresar notas" + "\n" + "2:Ver notas y sus estadisticas" + "\n" + "3:corregir nota")
print ("4:eliminar o añadir nota")

# Modos
# agregar notas


activate = 0
modo = int(input())
calificaciones = []
if modo == 1:
    print("cuantos estudiantes hay en su clase")
    estudiantes = 0
    numerodee = int(input())
    calificaciones = []
    print("agrege los valores de las notas")
    while estudiantes != numerodee:
        calificaciones.append(float(input()))
        estudiantes += 1
    print("las notas son", calificaciones)
else:
    print("ingrese primero las notas")
    sys.exit()
# Estadisticas
print("desea ver sus estadisticas?")
respuesta = input()
# Notas min max
if respuesta == "si":
    nmin = 10
    nmax = 0

    for i in calificaciones:
        if i < nmin:
            nmin = i
        if i > nmax:
            nmax = i
    print('la nota mas baja es = ', nmin, 'y la nota mas alta es de = ', nmax)
# Promedio
    suma = 0
    for m in calificaciones:
        suma += m

    print("el promedio es de ", suma/len(calificaciones))
else:
    print("gracias por usar este programa")
    sys.exit()

# Moda
print("la moda es", max(set(calificaciones), key=calificaciones.count))

# Correcion de notas
respuesta = input("desea corregir alguna nota?")
if respuesta == "si":
    numerodenota = int(input("cual nota desea cambiar"))
    nuevanota = float(input("ingrese la nueva nota"))
    calificaciones.insert(numerodenota, nuevanota)
    calificaciones.remove(numerodenota)
    print("las nuevas notas son : ", calificaciones)
else:
    print("gracias por usar este programa")
    sys.exit()

# Eliminar o agregar estudiantes

respuesta = input("Desea eliminar algun estudiante")

if respuesta == "si":
    numerodeestudiante = int(input("Que estudiante desea eliminar"))

    calificaciones.remove(calificaciones[numerodeestudiante-1])
    print("las nuevas notas son : ", calificaciones)
else:
    print("gracias por usar este programa")
    sys.exit()

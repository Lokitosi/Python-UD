
# variables

calificaciones = []
gentequepaso = []


def agregarnotas():
        numerodee = int(input("cuantos estudiantes hay en su clase"))
        estudiantes = 0
        print("agrege los valores de las notas")
        while estudiantes != numerodee:
            calificaciones.append(float(input()))
            estudiantes += 1
        print("las notas son", calificaciones, "\n")


def estadisticas():
    if len(calificaciones) == 0:
        print("No hay notas Disponibles",  "\n")
    else:

        nmin = 10
        nmax = 0

        for i in calificaciones:
            if i < nmin:
                nmin = i
            if i > nmax:
                nmax = i
        print('la nota mas baja es = ', nmin, 'y la nota mas alta es de = ', nmax, "\n")

        # promedio:

        suma = 0
        for m in calificaciones:
            suma += m
        print("el promedio es de ", suma/len(calificaciones))

        # Moda:

        print("la moda es", max(set(calificaciones), key=calificaciones.count), "\n")


def cambio_de_nota():
    if len(calificaciones) == 0:
        print("No hay notas Disponibles", "\n")
    else:
        numerodenota = int(input("cual nota desea cambiar"))
        nuevanota = float(input("ingrese la nueva nota"))
        calificaciones[numerodenota-1] = nuevanota
        print("las nuevas notas son : ", calificaciones, "\n")


def eliminarestudiante():
    if len(calificaciones) == 0:
        print("No hay notas Disponibles", "\n")
    else:
        numerodeestudiante = int(input("Que estudiante desea eliminar"))

        calificaciones.remove(calificaciones[numerodeestudiante - 1])
        print("las nuevas notas son : ", calificaciones, "\n")


def borrartodo():
    if len(calificaciones) == 0:
        print("No hay notas Disponibles", "\n")
    else:
        calificaciones.clear()
        print("usted ya no tiene notas, ingreselas de nuevo por favor", "\n")


def ustedpaso():
    if len(calificaciones) == 0:
        print("No hay notas Disponibles", "\n")
    else:
        for i in calificaciones:
            if i >= 3.5:
                print(i, " Aprobo ,", end= "")
            else:
                print(i, " perdio ,", end="")


def interfaz():
    print("MENU:"+"\n"+"Elija que opcion desea realizar")
    print("1.Agregar notas"+"\n"+"2.ver estadisticas"+"\n"+"3.cambiar notas")
    print("4.Eliminar notas"+"\n"+"5.Limpiar lista"+"\n"+"6.ver que personas aprobaron las materias")

    global seleccion
    seleccion = int(input())
    while seleccion != 7:
        if seleccion == 1:
            agregarnotas()
            interfaz()
        elif seleccion == 2:
            estadisticas()
            interfaz()
        elif seleccion == 3:
            cambio_de_nota()
            interfaz()
        elif seleccion == 4:
            eliminarestudiante()
            interfaz()
        elif seleccion == 5:
            borrartodo()
            interfaz()
        elif seleccion == 6:
            ustedpaso()
            interfaz()


interfaz()

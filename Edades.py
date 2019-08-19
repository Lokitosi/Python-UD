import random
# preguntar edad Aleatorio

personajes = 0

nompersonaje = ["Bart(10)", "Homero(39)", "maggie(1)", "Abe(86)", " Lisa(8)", "El ayudante de santa(8)", "marge(36)"]

nint1 = 0
nint2 = 0
nint3 = 0
f = 1
c = 1
k = 1


def aleatorio():
    global nint1
    global intentos

    print("\n", nompersonaje[personajes])
    print("a que puedo adivinar tu edad"+"escribe 1 para si y 0 para no")
    intentos = 1

    numeroshechos = []
    while True:
        num = random.randint(1, 86)

        respuesta = 0

        while respuesta != 1:
            if num in numeroshechos:
                num = random.randint(1, 86)
            else:
                numeroshechos.append(num)
                respuesta = 1

        print("tu edad es: ", num, "?")
        respuesta = int(input())

        if respuesta == 1:
            print("tu edad es :", num)
            print("me tomo ", intentos, "intentos")

            break
        intentos += 1


# ejercicio con mitades


def edadesmitad(minimo, maximo, nintentos):

    global nnintentos
    nnintentos = 1

    print("\n", nompersonaje[personajes])
    prueba = ((maximo-minimo)/2)+minimo
    pregunta = int(input("tu edad es mayor a: " + "%.2f" % round(prueba)+"?\n[1]Si \n[2]No \n[3]Es igual\n"))

    if prueba == 1 and pregunta == 2:
        print("error porque tu edad no se encuentra en el rango establecido")

    if pregunta == 1:
        minimo = prueba
        nintentos += 1
        edadesmitad(minimo, maximo, nintentos)
    if pregunta == 2:
        maximo = prueba
        nintentos += 1
        edadesmitad(minimo, maximo, nintentos)
    if pregunta == 3:
        nintentos += 1
        print("")
        print("ADIVINE TU EDAD!!!")
        print("Tu edad es: " + ("%.2f" % round(prueba)))
        nnintentos = int(nintentos)
        print("Numeros de preguntas realizadas: " + str(nintentos))


# THX jean :)

# Ejercicio con clave


def edadesclave():

    global cintentos

    cintentos = 1
    print("\n", nompersonaje[personajes])
    print("a que puedo adivinar tu edad" + "escribe 1 para si y 0 para no")
    clave = int(input("Cual es el ultimo digito de tu edad?"))
    while True:
        print("Tienes ", clave, "años?")
        respuesta = int(input())
        if respuesta == 1:
            print("tu edad es :", clave)
            print("me tomo ", cintentos, "intentos")
            break

        else:
            cintentos += 1
            clave += 10


# programa completo uniendo 3 metodos
def main():
    global nint1
    global personajes
    global intentos
    global nint2
    global nnintentos
    global cintentos
    global nint3
    global f
    global c
    global k

    print("Elija un metodo para adivinar la edad de:")
    print("1.Bart( 10 años), 2.Homero( 39 años), 3.maggie( 1 año)")
    print("4.Abe( 86 años), 5.Lisa( 8 años), 6.El ayudante de santa( 8 años), 7. Marge( 36 años)")
    print("Metodos:"+"\n"+"[1]Aleatorio"+"\n"+"[2]Mitades"+"\n"+"[3]Clave")
    metodo = int(input())
# metodo 1

    while f == 1 or c == 1 or k == 1:
        if metodo == 1:

            while personajes != 7:
                aleatorio()
                personajes += 1
                nint1 += intentos
            personajes = 0
            print("el promedio fue de ", (nint1 / 7))
            nint1 = (nint1 / 7)
            f = 0
            if f == 1 or c == 1 or k == 1:
                main()
            else:
                break


# metodo 2
        elif metodo == 2:

            while personajes != 7:
                edadesmitad(minimo=1, maximo=128, nintentos=0)
                personajes += 1
                nint2 += nnintentos
            personajes = 0
            print("el promedio fue de ", (nint2 / 7))
            nint2 = (nint2 / 7)
            c = 0
            if f == 1 or c == 1 or k == 1:
                main()
            else:
                break

# metodo 3
        elif metodo == 3:

            while personajes != 7:
                edadesclave()
                personajes += 1
                nint3 += int(cintentos)
            personajes = 0
            print("el promedio fue de ", (nint3 / 7))
            nint3 = (nint3 / 7)
            k = 0
            if f == 1 or c == 1 or k == 1:
                main()
            else:
                break

# eres subnormal
        elif metodo != 1 and metodo != 2 and metodo != 3:
            print("el metodo que selecciono es invalido")
            main()

    if nint1 < nint2 and nint1 < nint3:
        print("El metodo aleatorio es el mas efectivo")
    elif nint2 < nint1 and nint2 < nint3:
        print("El metodo fragmentado es el mas efectivo")
    elif nint3 < nint2 and nint3 < nint1:
        print("El metodo clave es el mas efectivo")
    print("Gracias por participar")


main()

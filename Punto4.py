import random
import time

q = int(input("Ingrese el numero de personajes: "))


def aleatorio():
    lista = []
    a = 0
    for i in range(1, 128):
        lista.append(i)

    while len(lista) > 0:
        numero = random.choice(lista)
        pregunta = input("Tu edad es " + str(numero) + "?\n"
                                                       "==>")
        a += 1
        if pregunta == "si":
            print("")
            print("Tu edad es " + str(numero) + " años")
            print("ADIVINE TU EDAD!!! ")
            print("Numero de preguntas realizadas: " + str(a))
            promedio_aleatorio.append(a)
            return a

        if pregunta == "no":
            orden = lista.index(numero)
            lista.remove(lista[orden])

def fragmentado(minimo, maximo, preguntas):
    prueba = ((maximo - minimo) / 2) + minimo
    pregunta = input("tu edad es mayor a: " + "%.2f" % round(
        prueba) + "?\nsi \nno \nesa es mi edad\n (escriba alguna de estas opciones)\n"
                  "==>")

    if (prueba == 1 and pregunta == 2):
        print("error porque tu edad no se encuentra en el rango establecido")
        while True:
            1 == 1
    if (pregunta == "si"):
        minimo = prueba
        preguntas += 1
        fragmentado(minimo, maximo, preguntas)
    if (pregunta == "no"):
        maximo = prueba
        preguntas += 1
        fragmentado(minimo, maximo, preguntas)
    if (pregunta == "esa es mi edad"):
        preguntas += 1
        print("")
        print("ADIVINE TU EDAD!!!")
        print("Tu edad es: " + "%.2f" % round(prueba) + " años")
        print("Numeros de preguntas realizadas: " + str(preguntas))
        promedio_fragmentado.append(preguntas)
        return preguntas

def clave():
    a = 1
    n = 0

    clave = int(input("Ingrese el ultimo digito de su edad:\n"
                      "==>"))
    edad = input("Su edad es: " + str(n) + str(clave) + "==>")
    a += 1
    for i in range(12):
        n += 1
        edad = input("Su edad es: " + str(n) + str(clave))
        a += 1
        if edad == "si":
            print(" ")
            print("Tienes " + str(n) + str(clave) + " años")
            print("ADIVINE TU EDAD!!!")
            print(" ")
            print("Numero de preguntas realizadas: " + str(a))
            promedio_clave.append(a)
            return a

def p_aleatorio():
    sum(promedio_aleatorio)/q

def p_fragmentado():
    sum(promedio_fragmentado)/q

def p_clave():
    sum(promedio_clave)/q

def promedios():
    print("El promedio de preguntas con el metodo aleatorio es de " + str(p_aleatorio()))
    print("El promedio de preguntas con el metodo fragmentado es de " + str(p_fragmentado()))
    print("El promedio de preguntas con el metodo clave-valor es de " + str(p_clave()))

def menu():
    print("")
    print("===============ADIVINA EDADES===============")
    print("")
    print(" Escoja una metodo para adivinar su edad:    ")
    print("1. Aleatorio\n"
          "2. Fragmentado\n"
          "3. Clave - Valor\n"
          "4. Promedios\n"
          "5. Salir")



while True:
    menu()
    promedio_aleatorio = []
    promedio_fragmentado = []
    promedio_clave = []
    personajes = 0
    opcionmenu = input("==>")
    for i in range (q):
            if opcionmenu == "1":
                print("")
                time.sleep(1.5)
                print("Personaje " + str(i+1))
                aleatorio()
                personajes +=1

            elif opcionmenu == "2":
                print("")
                time.sleep(1.5)
                print("Personaje " + str(i + 1))
                fragmentado(minimo=1, maximo=128, preguntas=0)
                personajes += 1

            elif opcionmenu == "3":
                print("")
                time.sleep(1.5)
                print("Personaje " + str(i + 1))
                clave()
                personajes += 1

            elif opcionmenu == "4":
                print("")
                time.sleep(1.5)
                promedios()
                break

            elif opcionmenu == "5":
                break

            else:
                print("Opcion incorrecta\n"
                      "Escoja alguna de las opciones del menu")



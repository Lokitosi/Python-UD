# ejercicio 1
name = input('¿Cual es tu nombre?')

print ("bienvenido a python, " + name)
edad = int(input("¿Cual es tu edad?"))

if edad <= 17:
    print(" eres menor de edad")
else :
    print('ya eres mayor de edad')

# ejercicio 2

print("dime un numero ctm")
x = int(input())

if x % 2 == 0:
    print("el numero es par")
else:
    print("el numero es impar")

# ejercicio 3

for i in range(100):
    i = i+1
    print(i)

# ejercicio 4

x = int(input())

numero = 0

for numero in range(11):
	if numero !=11:
		multiplicacion = numero*x
		print (x," X ",numero," = ",multiplicacion)
		numero+1

#ejercicio 5

numero1 = 0
numero2 = 0
for numero2 in range(11):
	if numero2 != 11:
		for numero1 in range(11):
			if numero1 != 11:
				multiplicacion = numero1*numero2
				print (numero1," X ",numero2," = ",multiplicacion)
				numero1 +1
		print("tabla del", numero2)
		numero2+1


# Ejercicio 6
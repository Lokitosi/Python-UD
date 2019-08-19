# -*- coding: cp1252 -*-
import random

def Question():
    intentos=0;listo=0;numeros=[0]
    while (listo==0):
        valorPrueba=random.randint(1,128)
        b=0
        while(b==0):
            for j in range (10000):
                for i in range(len(numeros)):
                    if(numeros[i]==valorPrueba):
                        valorPrueba=random.randint(1,128)
            b=1
        if(intentos==128):
            print("Error, porque ya mencionamos todo el rango")
            while True:
                1==1
        else:
            answer=int(input("Tu edad es "+ str(valorPrueba)+"?\n[1]Si \n[2]No\n"))
            if(answer==2):
                intentos+=1
                numeros.append(valorPrueba)
            elif(answer==1):
                intentos+=1
                listo=1
            return intentos
        

def Question2(minimo,maximo,intentos):
    prueba=((maximo-minimo)/2)+minimo
    pregunta=int(input("tu edad es mayor a: "+str(prueba)+"?\n[1]Si \n[2]No \n[3]Es igual\n"))

    if(prueba==1 and pregunta==2):
        print("error porque tu edad no se encuentra en el rango establecido")
        while True:
            1==1
    if(pregunta==1):
        minimo=prueba
        intentos+=1
        Question2(minimo,maximo,intentos)
    if(pregunta==2):
        maximo=prueba
        intentos+=1
        Question2(minimo,maximo,intentos)
    if(pregunta==3):
        intentos+=1
        return intentos
    

def Question3(minimo,maximo,intentos,cifra):
    prueba1=(((maximo-minimo)/2)+minimo)
    decenas=0
    redondeada=0
    for i in range (1000):
        if(prueba1>=10):
            decenas+=10
            prueba1-=10
    prueba=cifra+decenas
    pregunta=int(input("tu edad es mayor a: "+str(prueba)+"?\n[1]Si \n[2]No \n[3]Es igual\n"))
    if(prueba==cifra and pregunta==2):
        print("error porque tu edad no se encuentra en el rango establecido")
        while True:
            1==1
    if(pregunta==1):
        minimo=prueba
        intentos+=1
        Question3(minimo,maximo,intentos,cifra)
    if(pregunta==2):
        maximo=prueba
        intentos+=1
        Question3(minimo,maximo,intentos,cifra)
    if(pregunta==3):
        intentos+=1
        print("tu edad es: "+str(prueba)+" y se ha encontrado en "+str(intentos)+" intento(s)")
        return intentos


intentosMetodo1=0;intentosMetodo2=0;intentosMetodo3=0

for i in range(8):
    print("personaje "+ str(i+1))
    intentosMetodo1+=Question()
    print("siguiente metodo")
for i in range(8):
    print("personaje "+ str(i+1))
    intentosMetodo2+=Question2(1,128,0)
print("siguiente metodo")
for i in range(8):
    print("personaje "+ str(i+1))
    ans=int(input("En qué cifra termina la edad de tu personaje?"))
    intentosMetodo3+=Question3(1,128,0,ans)
print("RESULTADOS:")

if(intentosMetodo1<intentosMetodo2 and intentosMetodo1<intentosMetodo3):
    mejor="1"
if(intentosMetodo2<intentosMetodo1 and intentosMetodo2<intentosMetodo3):
    mejor="2"
if(intentosMetodo3<intentosMetodo2 and intentosMetodo3<intentosMetodo1):
    mejor="3"
    
print("Intentos promedio en: \nmetodo 1 : "+str(intentosMetodo1/8)+"\nmetodo 2 : "+str(intentosMetodo2/8)+"\nmetodo 3 : "+str(intentosMetodo3/8))
print("la mejor estrategia es la: "+ str(mejor))

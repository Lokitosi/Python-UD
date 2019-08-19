#!/usr/bin/env python
# coding: utf-8

# In[ ]:


### Nombre:Edison Andres Gamba Robayo    Codigo: 20191020170


# In[ ]:


### 1 EJERCICIO


# In[6]:


nombre = input ()
print ("hola mundo")
print ("Soy ",nombre,"¿como estas?")


# In[ ]:


### 2 EJERCICIO


# In[7]:


a= (int(input()))
b= (int(input()))

suma = (a+b)
resta = (a-b)
multiplicacion = (a*b)
division = (a/b)
divisionf = (a//b)
residuo = (a % b)

print (suma,resta,multiplicacion,division,divisionf,residuo)


# In[ ]:


### 3 ejercicio


# In[8]:


import math
print ("ingrese la base del rectangulo y despues su altura")
base = (int(input()))
altura = (int(input()))

area = (base*altura)
perimetro = ((base*2)+(altura*2))
diagonal = (math.sqrt(base**2+altura**2))

print (area ,perimetro,diagonal)


# In[ ]:


### 4 ejercicio


# In[10]:


a = ((input()))
b = (input())

p = (a and b)
q = (a or b)
z = (not a,not b)

print (p ,q ,z )


# In[ ]:


### 5 ejercicio


# In[11]:


a = (int(input()))

prueba = (a % 2)
if prueba ==0 :
    print("es par")
else :
    print ("no es par")


# In[ ]:


### 6 ejercicio


# In[12]:


a = (int(input()))

if a > 50 :
    print ("el numero es mayor a 50")
else:
    if a == 50:
        print ("el numero es 50")
    else:
        print("el numero es menor que 50")
        


# In[ ]:


### 7 ejercicio


# In[13]:


a = (int(input()))
b = (int(input()))

if a > b :
    print ("el segundo numero es menor que el primero")
else:
    if a == b:
        print ("ambos numeros son iguales")
    else:
        print("el segundo numero es mayor que el primero")


# In[ ]:


### 8 ejercicio


# In[ ]:


for numeros in range (1,101):
    print (numeros)


# In[ ]:


### 9 ejercicio


# In[ ]:


for x in range (1,15):
    print (2*x+1)


# In[ ]:


### 10 ejercicio


# In[ ]:


for x in range (1,201):
    if (x % 10 == 0):
        print (x)


# In[ ]:


### 11 ejercicio


# In[ ]:


print("ingrese dos numeros")

a = int(input())
b = int(input())

multiplicacion = 1

for contador in range (a,b):
    
   multiplicacion = multiplicacion * contador
   print(multiplicacion)
    
    


# In[ ]:


### 12 ejercicio


# In[ ]:


a= int(input())
i= 0
for l in range (a):
    if i!= a:
        print ("@"*a)
        i+1
    
        
    


# In[ ]:


### 13 ejercicio


# In[1]:


a= int(input())
i= 0
c = 0
d= a-4

if i!=1:
    print ("@"*a)
    i+1
for x in range (a-2):
    if c!= a-2:
        print ("@"," "*(d),"@")
        c+1
print ("@"*a)
    
            


# In[ ]:


### 14 ejercicio


# In[7]:


num = 2 
for i in range(1,11):
      print(i,"x",num,"=",i*num) 


# In[ ]:


### 15 ejercicio


# In[ ]:


print("escribe un numero que no sea negativo")
a= int(input())
while a>0:
    a= int(input())
    


# In[ ]:


### 16 ejercicio


# In[ ]:


print ("a partir de aqui no los logre hacer.")


# In[ ]:





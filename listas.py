notas=[4.5,2.5,3.5,2.5,5,2.2,3.5,3.5,4.3,5,0,0,0,0,0,0,0,0,0,0]

nmin=0
nmax=0

for i in notas:
    if (i < nmin):
        nmin=i
    if (i> nmax):
        nmax=i

for i in notas:
    a=i+i
print('la nota mas baja es = ',nmin,'la nota mas alta es de = ',nmax)
print('el promedio es de', a)

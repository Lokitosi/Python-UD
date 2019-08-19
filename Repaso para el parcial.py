print (" X |", end=" ")
for i in range(1,11):
    print ("%2d" % (i),end=" "),
print ("\n", "-"*35)

for i in range(1,11):
    print ("%2d |" % (i),end= " "),
    for j in range(1,11):
        print ("%2d" % (i*j),end=" ")
    print(" ")


import turtle

pipo = turtle.Turtle()
cerrar = 0


def figura():
    lados = turtle.numinput("Lados", "Ingrese cuantos lados tendra la figura:")
    tamaño = turtle.numinput("Tamaño", "Ingrese el tamaño de la figura:")
    relleno = turtle.textinput("relleno", "Desea rellenar la figura")
    pipo.clear()
    pipo.color("#1AB231", "#19EC38")
    pipo.begin_fill()
    pipo.pensize(5)
    for i in range(int(lados)):
        pipo.forward(tamaño)
        pipo.right(-360/lados)
        turtle.color("black", "red")
    if relleno == "si":
        pipo.end_fill()


while cerrar == 0:
    figura()

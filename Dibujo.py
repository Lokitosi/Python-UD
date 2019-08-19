import turtle
pipo = turtle.Turtle()

def cuadrado(lado):
    pipo.clear()
    turtle.shape("turtle")

    for i in range(4):
        pipo.forward(lado)
        pipo.right(90)


def cuadradosconsecutivos():
    pipo.clear()
    turtle.shape("turtle")
    for lado in range(50,500,50):
        cuadrado(lado)
    turtle.exittoclick()


def triangulo(lado=100):
    for i in range(3):

        pipo.forward(lado)
        pipo.right(-120)





def pentagono():
    for i in range(5):
        pipo.color()
        pipo.forward(100)
        pipo.right(-72)


def circulo():
    for i in range(720):
        pipo.color()
        pipo.forward(1)
        pipo.speed(0.1)
        pipo.right(0.5)


def iniciar():
    turtle.shape("turtle")
    pipo.speed(1)
    turtle.onkey(cuadrado, "c")
    turtle.onkey(triangulo, "t")
    turtle.listen()


def main():
    iniciar()
    turtle.exitonclick()


circulo()
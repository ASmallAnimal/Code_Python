import turtle
def koch(size,n):
    if n==0:
        turtle.fd(size)
    else:
        for angle in [0,90,-90,-90,90]:
            turtle.left(angle)
            koch(size/3,n-1)
def main():
    turtle.setup(600,600)
    turtle.penup()
    turtle.goto(-200,150)
    turtle.pendown()
    turtle.pensize(2)
    level=3
    koch(320,level)
    turtle.right(90)
    koch(320,level)
    turtle.right(90)
    koch(320,level)
    turtle.right(90)
    koch(320,level)
    turtle.hideturtle()
    turtle.done()
main()

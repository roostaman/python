import turtle as t

ron_turtle = t.Turtle()
screen = t.Screen()


def move_forward():
    ron_turtle.forward(50)


screen.onkey(fun=move_forward, key='space')
screen.listen()

screen.exitonclick()

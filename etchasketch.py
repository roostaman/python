import turtle as t

ron_turtle = t.Turtle()
screen = t.Screen()


def move_forward():
    ron_turtle.forward(20)


def move_backward():
    ron_turtle.backward(20)


def turn_left():
    ron_turtle.left(15)


def turn_right():
    ron_turtle.right(15)


def clear():
    ron_turtle.clear()
    ron_turtle.penup()
    ron_turtle.home()
    ron_turtle.pendown()


screen.listen()
screen.onkey(fun=move_forward, key='w')
screen.onkey(fun=move_backward, key='s')
screen.onkey(fun=turn_left, key='a')
screen.onkey(fun=turn_right, key='d')
screen.onkey(fun=clear, key='c')

screen.exitonclick()

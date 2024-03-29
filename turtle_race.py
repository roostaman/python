import turtle as t
import random

screen = t.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter a color: ")

is_race_on = False
colors = ["orange", "blue", "grey", "red", "green", "purple"]
racer_list = []
positions = [-100, -60, -20, 20, 60, 100]

for i in range(6):
    new_racer = t.Turtle(shape="turtle")
    new_racer.penup()
    new_racer.color(colors[i])
    new_racer.goto(x=-230, y=positions[i])
    racer_list.append(new_racer)


def go_race():
    for racer in racer_list:
        if racer.xcor() > 230:
            winner_color = racer.pencolor()
            if winner_color == user_bet:
                print(f"You've won! The {winner_color} turtle is the winner!")
            else:
                print(f"You've lost. The {winner_color} turtle is the winner!")
            return False
        go_num = random.randint(0, 10)
        racer.forward(go_num)
    return True


if user_bet:
    is_race_on = True

while is_race_on:
    is_race_on = go_race()

screen.exitonclick()

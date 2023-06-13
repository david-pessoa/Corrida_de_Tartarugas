from turtle import Turtle, Screen
from random import randint
colors = ["red", "blue", "green", "purple", "orange"]
winner = ""
turtle_dict = dict()
screen = Screen()
screen.setup(height = 600, width = 700)
screen.title("Turtle Race!")
bet = screen.textinput(title = "Make your bet", prompt = "Choose a turtle. Insert the color").lower()
start_pos = (-290, 300)
space = 100

for turtle in colors:
    turtle_dict[turtle] = Turtle(shape="turtle")
    turtle_dict[turtle].penup()
    turtle_dict[turtle].color(turtle)
    turtle_dict[turtle].setpos(start_pos[0], start_pos[1] - len(turtle_dict) * space)
    turtle_dict[turtle].pendown()

while not winner:
    for turtle in colors:
        distance = randint(0, 10)
        turtle_dict[turtle].forward(distance)
        if turtle_dict[turtle].pos()[0] >= 290:
            winner = turtle_dict[turtle].pencolor()
            break

positions = dict()
pos_list = list()
for turtle in colors:
    positions[turtle] = turtle_dict[turtle].pos()[0]
    pos_list.append(positions[turtle])
    print(positions[turtle])
pos_list.sort()
pos_list.reverse()
print(pos_list)
user_graph_pos = positions[bet]
user_podium_pos = pos_list.index(user_graph_pos) + 1

if winner == bet:
    screen.textinput("You win!", "Congratulations, you won the race!")
else:
    if user_podium_pos == 2:
        fstring = "2nd"
    elif user_podium_pos == 3:
        fstring = "3rd"
    else:
        fstring = str(user_podium_pos) + "th"
    screen.textinput("You loose!", f"Your turtle is the " + fstring)

screen.exitonclick()
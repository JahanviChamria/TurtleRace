from turtle import Turtle, Screen
import random
race=False

screen=Screen()
screen.setup(500, 400)
colors=["red", "yellow", "orange", "blue", "green", "purple"]
pos=[-100, -50, 0, 50, 100, 150]
t=[]
for n in range(0,6):
    a = Turtle()
    a.shape("turtle")
    a.color(colors[n])
    a.penup()
    a.goto(x=-230, y=pos[n])
    t.append(a)

bet=screen.textinput(title="Make your bet:", prompt="Which turtle will win the race? ")
if bet:
    race=True

while race:

    for tu in t:
        if tu.xcor()>230:
            race=False
            winner=tu.pencolor()
        x = random.randint(0, 10)
        tu.forward(x)

if winner==bet:
    print("Your turtle has won!")
else:
    print(f"You lose! The {winner} turtle won the race.")












screen.exitonclick()
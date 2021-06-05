from turtle import Turtle, Screen
import random
is_race_on = False
screen = Screen()
# setting up the screen height and width
screen.setup(width=500, height=400)

# taking the bet at the beggining of the race
user_bet = screen.textinput(title="Make your bet", prompt="which turtle will win the race")
# print(user_bet)
colors = ["red", "green", "blue", "yellow", "purple", "orange"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtles = []

# to create different turtle at different coordinance with different color
for turtle_index in range(0, 5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.speed(1)
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-235, y=y_position[turtle_index])
    all_turtles.append(new_turtle)
# starting the race
if user_bet:
    is_race_on = True
# creating the loop to run the race
while is_race_on:
    # ending the race
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            # selecting the winner
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've WON! The {winning_color} turtle is the winner!")
            else:
                print(f"You've LOST! The {winning_color} turtle is the winner!")
        # creating the random movement for different turtles
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)



























screen.exitonclick()
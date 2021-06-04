# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [
                (26, 108, 164),
                (194, 38, 81),
                (237, 161, 50),
                (234, 215, 86),
                (226, 237, 229),
                (223, 137, 176),
                (143, 108, 57),
                (102, 197, 219),
                (205, 166, 30),
                (21, 57, 132),
                (214, 74, 91),
                (238, 89, 49),
                (119, 192, 140),
                (142, 208, 227),
                (4, 185, 176),
                (106, 108, 198),
                (138, 29, 72),
                (5, 161, 86),
                (98, 51, 36),
                (23, 156, 209),
                (229, 167, 185),
                (173, 185, 222),
                (29, 90, 95),
                (233, 172, 162),
                (155, 212, 190),
                (88, 46, 33),
                (244, 207, 5)
            ]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()
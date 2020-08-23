# Turtle
import turtle
my_turtle = turtle.Turtle()
def Square(length,angle):
    for i in range(4):
        my_turtle.forward(length)
        my_turtle.left(angle)


for i in range(50):
    Square(200,90)
    my_turtle.left(23)
turtle.speed(1)

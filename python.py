from turtle import *

turtle = Turtle()
turtle.color('green', 'red')
turtle.speed(50)

def draw_star(n, size):
    if n % 2 == 0:
        print(" No odd number for n.")
        return
    
    angle = 180 - (180 / n) 
    
    for i in range(n):
        turtle.forward(size)
        turtle.right(angle)


turtle.penup()
turtle.goto(-40, 0)
turtle.pendown()
draw_star(19, 150)


turtle.penup()
turtle.goto(100, 0)  
turtle.pendown()
draw_star(51, 150)

turtle.hideturtle()
done()

#something

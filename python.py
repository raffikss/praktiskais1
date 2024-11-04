from turtle import *
#Configuration settings for turtle
turtle = Turtle()
turtle.color('green', 'red')
turtle.speed(50)

def draw_star(n, size):
    if n % 2 == 0:
        print(" No odd number for n.") # This function calculates the stars points, and doesn't let it be an odd number of points
        return
    
    angle = 180 - (180 / n) 
    
    for i in range(n):
        turtle.forward(size)
        turtle.right(angle)


turtle.penup()
turtle.goto(-40, 0)  #Goes to the start coordinates
turtle.pendown()
draw_star(19, 150) # Makes the star - parameters are given in the brackets


turtle.penup()
turtle.goto(100, 0)   #Goes to the start coordinates
turtle.pendown()
draw_star(51, 150) # Makes the star - parameters are given in the brackets

turtle.hideturtle() #Hides the turtle
done()

#something

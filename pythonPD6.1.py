import turtle
import math
import time
import random

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Solar System Crash situation")

turtle.hideturtle()

class Sun:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def draw(self):
        sun_turtle = turtle.Turtle()
        sun_turtle.shape("circle")
        sun_turtle.color("yellow")
        sun_turtle.shapesize(stretch_wid=self.size, stretch_len=self.size)
        sun_turtle.penup()
        sun_turtle.goto(0, 0)
        sun_turtle.stamp()  

class Planet:
    def __init__(self, name, size, distance, color, orbit_speed, has_moon=False, moon_distance=20, moon_size=0.5, moon_orbit_speed=2):
        self.name = name
        self.size = size
        self.distance = distance
        self.color = color
        self.orbit_speed = orbit_speed  
        self.has_moon = has_moon
        self.moon_distance = moon_distance
        self.moon_size = moon_size
        self.moon_orbit_speed = moon_orbit_speed
        self.angle = 0  #
        self.moon_angle = 0  

        self.planet_turtle = turtle.Turtle()
        self.planet_turtle.shape("circle")
        self.planet_turtle.color(self.color)
        self.planet_turtle.shapesize(stretch_wid=self.size, stretch_len=self.size)
        self.planet_turtle.penup()  
        self.planet_turtle.goto(self.distance, 0)  
        self.planet_turtle.pendown()  

        if self.has_moon:
            self.moon_turtle = turtle.Turtle()
            self.moon_turtle.shape("circle")
            self.moon_turtle.color("grey")
            self.moon_turtle.shapesize(stretch_wid=self.moon_size, stretch_len=self.moon_size)
            self.moon_turtle.penup()  
            self.moon_turtle.goto(self.planet_turtle.xcor() + self.moon_distance, self.planet_turtle.ycor())  #
            self.moon_turtle.pendown()

    def update_position(self):
        x = self.distance * math.cos(math.radians(self.angle))
        y = self.distance * math.sin(math.radians(self.angle))
        self.planet_turtle.goto(x, y)

        if self.has_moon:
            moon_x = x + self.moon_distance * math.cos(math.radians(self.moon_angle))
            moon_y = y + self.moon_distance * math.sin(math.radians(self.moon_angle))
            self.moon_turtle.goto(moon_x, moon_y)

            self.moon_angle += self.moon_orbit_speed
            if self.moon_angle >= 360:
                self.moon_angle -= 360

        self.angle += self.orbit_speed
        if self.angle >= 360:
            self.angle -= 360

def draw_stars(num_stars):
    star_turtle = turtle.Turtle()
    star_turtle.hideturtle()
    star_turtle.speed(0)
    star_turtle.color("yellow")
    star_turtle.penup()
    screen.tracer(0)

    for _ in range(num_stars):
        x = random.randint(-400, 400)
        y = random.randint(-400, 400)
        star_turtle.goto(x, y)
        star_turtle.dot(random.randint(1, 3)) 
    screen.update()

def draw_milky_way():
    milky_way_turtle = turtle.Turtle()
    milky_way_turtle.hideturtle()
    milky_way_turtle.speed(0)
    milky_way_turtle.color("grey")
    screen.tracer(0)

    for _ in range(50):
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        milky_way_turtle.penup()
        milky_way_turtle.goto(x, y)
        milky_way_turtle.dot(random.randint(4, 7), "lightgrey")

    screen.update()

class Meteorite:
    def __init__(self):
        self.meteorite_turtle = turtle.Turtle()
        self.meteorite_turtle.shape("circle")
        self.meteorite_turtle.color("red")
        self.meteorite_turtle.shapesize(stretch_wid=0.3, stretch_len=0.3)
        self.meteorite_turtle.penup()
        self.meteorite_turtle.speed(0)
        self.reset_position()

    def reset_position(self):
        self.meteorite_turtle.goto(random.randint(-400, 400), 300)
        self.meteorite_turtle.setheading(random.randint(200, 250)) 

    def update_position(self):
        self.meteorite_turtle.forward(10)
        if self.meteorite_turtle.ycor() < -300:
            self.reset_position()

def main():
    draw_stars(100)

    draw_milky_way()

    sun = Sun(name="Sun", size=3)
    sun.draw()

    mercury = Planet(name="Mercury", size=0.5, distance=60, color="grey", orbit_speed=4)
    venus = Planet(name="Venus", size=1, distance=100, color="orange", orbit_speed=2)
    earth = Planet(name="Earth", size=1.2, distance=150, color="green", orbit_speed=1, has_moon=True, moon_distance=20, moon_orbit_speed=5)
    mars = Planet(name="Mars", size=0.8, distance=200, color="red", orbit_speed=0.5)

    planets = [mercury, venus, earth, mars]

    meteorites = [Meteorite() for _ in range(5)]

    while True:
        for planet in planets:
            planet.update_position()

        for meteorite in meteorites:
            meteorite.update_position()

        screen.update()  
        time.sleep(0.05)  

    turtle.done()

if __name__ == "__main__":
    screen.tracer(0)  
    main()

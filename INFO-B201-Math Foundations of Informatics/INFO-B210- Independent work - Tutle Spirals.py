
# Neel Sangani
# Independent work - Tutle Spirals

# Case Study Interface Design Excercises

# Exercise 5 - Archimedian Spiral

import turtle


def draw_spiral(t, n, length=3, a=0.1, b=0.0002): #assigned value to the parameters
    """Draws an Archimedian spiral starting at the origin.

    Args:
      n: how many line segments to draw
      length: how long each segment is
      a: how loose the initial spiral starts out (larger is looser)
      b: how loosly coiled the spiral is (larger is looser)

    http://en.wikipedia.org/wiki/Spiral
    """
    theta = 0.0 

    for i in range(n):
        t.fd(length) 
        dtheta = 1 / (a + b * theta)

        t.lt(dtheta)
        theta += dtheta #theta + dtheta. At one point will reach 0 to end the spiral

# Exercise 3 - Polygon Structures

import turtle
import math

def draw_pie(t, n, r):
    """Draws a pie, then moves into position to the right.

    t: Turtle
    n: number of segments
    r: length of the radial spokes
    """
    polypie(t, n, r) #calling polypie function
    t.pu()  #Pull up the pen, drawing
    t.fd(r*2 + 10) #minimum segment length 10
    t.pd() #pen down, no drawing

    
def polypie(t, n, r):
    """Draws a pie divided into radial segments.

    t: Turtle
    n: number of segments
    r: length of the radial spokes
    """
    angle = 360.0 / n 
    for i in range(n): #repeat the loop n times; n=segments
        isosceles(t, r, angle/2) #calling isosceles function
        t.lt(angle)  #left turn at user provided angle 


def isosceles(t, r, angle):
    """Draws an icosceles triangle.

    The turtle starts and ends at the peak, facing the middle of the base.

    t: Turtle
    r: length of the equal legs
    angle: peak angle in degrees
    """
    y = r * math.sin(angle * math.pi / 180)

    t.rt(angle) #right turn
    t.fd(r) #forward
    t.lt(90+angle) #left turn; add 'angle' to 90 
    t.fd(2*y)
    t.lt(90+angle)
    t.fd(r)
    t.lt(180-angle)

bob = turtle.Turtle()

bob.pu() 
bob.bk(130) #backwards 
bob.pd()

# draw polypies with various number of sides

size = 40
draw_pie(bob, 5, size) #calling the function draw_pie; assigned
                       #bob variable that calls turtle; number of sides,
                       #and length of the segments 
draw_pie(bob, 6, size)
draw_pie(bob, 7, size)

bob.invisible() #hides the turtle after making the patterns
turtle.mainloop() #allows turtle to call functions and run the command

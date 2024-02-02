# Neel Sangani
# Assignment 3 - String Manipulation; String methods

# Functions Exercises:

# Exercise 1 #############################################################

def right_justify(s):
    """
    Takes a string named s as a parameter and prints the string
    with enough leading spaces so that the last letter of the string is
    in column 70 of the display.

    Parameters:
    - s (str): Input string.

    Returns:
    None
    """
    concate = " " * 70 + s
    print(concate)

right_justify('Monty')

# Exercise 2 #############################################################

def do_twice(f, v):
    """
    Takes a function object, f, and a value, v as an argument and calls it twice.

    Parameters:
    - f (function): Function object to be called.
    - v: Value to be passed to the function.

    Returns:
    None
    """
    f(v)
    f(v)

def print_spam(v):
    """
    Prints the v parameter one time.

    Parameters:
    - v: Value to be printed.

    Returns:
    None
    """
    print(v)

do_twice(print_spam, 'spam')

def do_four(f, v):
    """
    Takes a function object, f, and a value, v and calls the function four times, passing value as a parameter.

    Parameters:
    - f (function): Function object to be called.
    - v: Value to be passed to the function.

    Returns:
    None
    """
    do_twice(f, v)
    do_twice(f, v)

do_four(print_spam, 'spam')

# Exercise 3 #############################################################

def design():
    """
    Prints a design line for a 4x4 grid.

    Returns:
    None
    """
    print("+", "- " * 4 + "+", "- " * 4 + "+")

def design_two(n):
    """
    Prints the second part of the design line for a 4x4 grid.

    Parameters:
    - n: Number of times to repeat the second part.

    Returns:
    None
    """
    for i in range(n):
        print("/", " " * 8 + "/", " " * 8 + "/")

def block():
    """
    Prints a 4x4 grid using the design and design_two functions.

    Returns:
    None
    """
    design()
    design_two(4)
    design()
    design_two(4)
    design()

block()

def design_three():
    """
    Prints a design line for a 4x4 grid.

    Returns:
    None
    """
    print("+", "- " * 4 + "+", "- " * 4 + "+", "- " * 4 + "+", "- " * 4 + "+")

def design_four(n):
    """
    Prints the second part of the design line for a 4x4 grid.

    Parameters:
    - n: Number of times to repeat the second part.

    Returns:
    None
    """
    for i in range(n):
        print("/", " " * 8 + "/", " " * 8 + "/", " " * 8 + "/", " " * 8 + "/")

def blockbuster():
    """
    Prints a 4x4 grid using the design_three and design_four functions.

    Returns:
    None
    """
    for value in range(4):
        design_three()
        design_four(4)
    design_three()

blockbuster()

# Case Study Interface Design Exercises:

# Exercise 2 #############################################################

import turtle
from math import pi

def square(t, length):
    """
    Draws a square with sides of the given length.

    Returns the Turtle to the starting position and location.

    Parameters:
    - t (turtle.Turtle): Turtle object.
    - length (int): Length of each side.

    Returns:
    None
    """
    for i in range(4):
        t.fd(length)
        t.lt(90)

def polyline(t, n, length, angle):
    """
    Draws n line segments.

    Parameters:
    - t (turtle.Turtle): Turtle object.
    - n (int): Number of line segments.
    - length (int): Length of each segment.
    - angle (float): Degrees between segments.

    Returns:
    None
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t, n, length):
    """
    Draws a polygon with n sides.

    Parameters:
    - t (turtle.Turtle): Turtle object.
    - n (int): Number of sides.
    - length (int): Length of each side.

    Returns:
    None
    """
    angle = 360.0/n
    polyline(t, n, length, angle)

def arc(t, r, angle):
    """
    Draws an arc with the given radius and angle.

    Parameters:
    - t (turtle.Turtle): Turtle object.
    - r (int): Radius.
    - angle (float): Angle subtended by the arc, in degrees.

    Returns:
    None
    """
    arc_length = 2 * pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n

    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)

def circle(t, r):
    """
    Draws a circle with the given radius.

    Parameters:
    - t (turtle.Turtle): Turtle object.
    - r (int): Radius.

    Returns:
    None
    """
    arc(t, r, 360)

def petal(t, r, angle):
    """
    Draws a petal using two arcs.

    Parameters:
    - t (turtle.Turtle): Turtle object.
    - r (int): Radius of the arcs.
    - angle (float): Angle (degrees) that subtends the arcs.

    Returns:
    None
    """
    for i in range(2):
        arc(t, r, angle)
        t.lt(180-angle)


def flower(t, n, r, angle):
    """
    Draws a flower with n petals.

    Parameters:
    - t (turtle.Turtle): Turtle object.
    - n (int): Number of petals.
    - r (int): Radius of the arcs.
    - angle (float): Angle (degrees) that subtends the arcs.
    
    Returns:
    None
    """
    for i in range(n):
        petal(t, r, angle)
        t.lt(360.0/n)

def move(t, length):
    """
    Move Turtle (t) forward (length) units without leaving a trail.
    Leaves the pen down.

    Parameters:
    - t (turtle.Turtle): Turtle object.
    - length (int): Units to move forward.

    Returns:
    None
    """
    t.pu()  # stop drawing
    t.fd(length)
    t.pd()  # drawing

bob = turtle.Turtle()

# draw a sequence of three flowers, as shown in the book.
move(bob, -100)  # setting the position of the turtle
flower(bob, 7, 60.0, 60.0)  # calling the function and assigning petal sides, radius, and angle

move(bob, 100)
flower(bob, 10, 40.0, 80.0)

move(bob, 100)
flower(bob, 20, 140.0, 20.0)

bob.hideturtle()
turtle.mainloop()

def TowerOfHanoi(n, from_rod, to_rod, aux_rod):
    """
    Tower of Hanoi is a mathematical puzzle where we have three rods and n disks.
    The objective of the puzzle is to move the entire stack to another rod, obeying the following simple rules:
    1) Only one disk can be moved at a time.
    2) Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack
    i.e. a disk can only be moved if it is the uppermost disk on a stack.
    3) No disk may be placed on top of a smaller disk.

    Source: https://www.geeksforgeeks.org/python-program-for-tower-of-hanoi/

    Parameters:
    - n (int): Number of disks.
    - from_rod (str): Source rod.
    - to_rod (str): Destination rod.
    - aux_rod (str): Auxiliary rod.

    Returns:
    None
    """
    if n == 1:  # Always moves the first aka smallest ring from A to B
        print("Move disk 1 from rod", from_rod, "to rod", to_rod)
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)  # Recursive Step with n-1
    # In this case order of parameters is switched so the Ring goes from A to C
    print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)  # Here again the parameter is changed
    # It goes from C to B

# The parameters were switched to keep the output readable - from_rod to to_rod layout
# n-1 and two recursive calls make sure that a large ring is never placed on a small ring

n = 3  # number of rings
TowerOfHanoi(n, 'A', 'B', 'C')  # A, B, C are the names of the rods

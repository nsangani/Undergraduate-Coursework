# Neel Sangani
# Assignment 5 - Loops: for and while

# Exercise 1

import math

def mysqrt(a):
    """
    Calculates the square root of a using Newton's method.

    Parameters:
    - a (float): Number to find the square root of.

    Returns:
    float: Square root of the given number.
    """
    x = a / 2
    while True:
        y = (x + a/x) / 2.0
        if abs(y - x) < 0.0000001:
            break
        x = y
    return x

def test_square_root(list_of_a):
    """
    Compares the results of mysqrt(a) and math.sqrt(a) for a list of values.

    Parameters:
    - list_of_a (list): List of values to test.

    Returns:
    None
    """
    line1a = "a"
    line1b = "mysqrt(a)"
    line1c = "math.sqrt(a)"
    line1d = "diff"

    line2a = "-"
    line2b = "---------"
    line2c = "------------"
    line2d = "----"

    spacing1 = " "
    spacing2 = " " * 3
    spacing3 = ""

    print(line1a, spacing1, line1b, spacing2, line1c, spacing3, line1d)
    print(line2a, spacing1, line2b, spacing2, line2c, spacing3, line2d)

    for a in list_of_a:
        col1 = float(a)
        col2 = mysqrt(a)
        col3 = math.sqrt(a)
        col4 = abs(mysqrt(a) - math.sqrt(a))

        print(col1, "{:<13f}".format(col2), "{:<13f}".format(col3), col4)

test_square_root(range(1, 10))


# Exercise 2

def eval_loop():
    """
    Iteratively prompts the user, takes the resulting input, evaluates it using eval,
    and prints the result. It should continue until the user enters 'done', and then return the value of the last expression it evaluated.

    Returns:
    None
    """
    while True:
        n = input("Calculate: ")
        if n == 'done':
            break
        else:
            result = eval(n)
            print(result)
    print(result)  # after breaking, print the last calculation

eval_loop()


# Exercise 3

def factorial(n):
    """
    Computes factorial of n recursively.

    Parameters:
    - n (int): Number to calculate the factorial of.

    Returns:
    int: Factorial of the given number.
    """
    if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        return result

def estimate_pi():
    """
    Computes an estimate of pi using an iterative formula.

    Returns:
    float: Estimated value of pi.
    """
    total = 0
    k = 0
    factor = 2 * math.sqrt(2) / 9801
    while True:
        num = factorial(4*k) * (1103 + 26390*k)
        den = factorial(k)**4 * 396**(4*k)
        term = factor * num / den
        total += term

        if abs(term) < 1e-15:
            break
        k += 1

    return 1 / total

print(estimate_pi())


# Chapter 8 Exercises

# Exercise 2

string = 'banana'
print(string.count('a'))

# Exercise 4

# Function definitions are already provided with comments explaining their behavior.


# Exercise 5

def rotate_word(word, num_shift):
    """
    Uses Ceasar cipher to encrypt given word using given shift.

    Parameters:
    - word (str): Word to be encrypted.
    - num_shift (int): Number of positions to shift.

    Returns:
    str: Encrypted word.
    """
    rotated_word = ''
    for l in word:
        rotated_word += chr(ord(l) + num_shift)
    return rotated_word

print(rotate_word('cheer', 7))
print(rotate_word('IBM', -1))




















































































































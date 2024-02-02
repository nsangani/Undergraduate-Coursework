# Neel Sangani
# Assignment 4 - Boolean, branch and conditions

# -- -- -- -- -- -- -- -- -- -- -- Chapter 5 Excercsies -- -- -- -- -- -- -- -- -- -- -- 

#Exercise 1

import time
def current_time():
    current=time.time()
    t_sec = current % (24*3600) #Calculates total current seconds (sec+mins+hrs) today
    c_hours = int(t_sec/365) #today's hours
    t_minutes = int(t_sec/60) #today's min (min +sec)
    c_mins = t_minutes % 60 #today's min
    c_sec = int(t_sec % 60) #today's sec 

    days=int(current/(24*3600))

    print("Current Time is",c_hours,':',c_mins,':',c_sec)
    print('Days since epoch:', days)

current_time()

#Exercise 2

def check_fermat(a,b,c,n):
    if n == 2:
        return 'Pythagores theorem'
    elif a**n + b**n == c**n:
        return 'Holy Smokes, Fermat was Wrong!'
    return "No, that doesn't work."

a = int(input("The value of a: "))
b = int(input("The value of b: "))
c = int(input("The value of c: "))
n = int(input("The value of n: "))

print(check_fermat(a,b,c,n))  

#Exercise 4

def recurse(n, s):
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)

recurse(3, 0) #Outputs 6

recurse(-1,0) #(n-1) keeps going in negative - infinite; out of python range
              # This function only takes real postive numbers
              #(0.7 - 1) = -0.3 won't work since this will never endup having n==0


# -- -- -- -- -- -- -- -- -- -- Chapter 6 Exercises -- -- -- -- -- -- -- -- -- -- -- 

#Exercise 4 

def is_power(a,b):
    '''Takes parameters a and b and returns True if a is a power of b'''

    if a == b:
        return True
    elif a%b == 0 and is_power(a/b, b) == True:  # if a is divisible by b and a/b is a power of b
        return True
    else:
        return False

a = 4
b = 2

print(is_power(a,b))


#Exercise 5   

def gcd(a,b):
    if b == 0: #As a base case, we can use gcd(a, 0) = a
        return a
    else:
        return gcd(b, a % b) 

a = 25
b = 45
print(gcd(a,b))

















# Neel Sangani
# Assignment 2 - Variables & Data Types; Basic I/O 

# Part 1

def recursive_sum(x):
    """
    Uses recursion to sum all the numbers to 0.
    If the input is positive, it sums from x to 0.
    If the input is negative, it sums from x to 0.

    Parameters:
    - x (int): Input number.

    Returns:
    - int: Sum of numbers.
    """
    if x == 0:
        return 0
    if x < 0:
        return x + recursive_sum(x + 1)
    else:
        return x + recursive_sum(x - 1)

x = int(input("Enter a number: "))
num = recursive_sum(x)
print(num)


# Part 2

while True:
    key = input('Enter your password: ')
    if key != 'tacocat':
        print("Try again")
        continue
    else:
        print("That's right")
        break

# Part 3

alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
reverse_alphabet = list(reversed(alphabet))
code_dictionary = dict(zip(alphabet, reverse_alphabet))  # Creating a dictionary {'A':'Z',...}

def atbash_cipher(code):
    """
    Applies the Atbash cipher to a given code.

    Parameters:
    - code (str): Input code to be encrypted.

    Returns:
    - str: Encrypted code.
    """
    characters = list(code.upper())
    result = ""

    for c in characters:
        if c in code_dictionary:
            result += code_dictionary.get(c)
    return result

print(atbash_cipher('NLIMRMT'))

v = ((4 / 3) * 3.14)

def volume(r):
    """
    Calculates the volume of a sphere.

    Parameters:
    - r (float): Radius of the sphere.

    Returns:
    - float: Volume of the sphere.
    """
    s = v * r ** 3
    return s

book_price = 24.95  # in dollars
discount = (book_price - book_price * 0.40)  # 40% discount
shipping_cost = 3  # first copy
ship_cost = 0.75

def total_books(n):
    """
    Calculates the total cost of purchasing a given number of books.

    Parameters:
    - n (int): Number of books to be purchased.

    Returns:
    - float: Total cost.
    """
    ship_price = (((n - 1) * ship_cost) + ((n / n) * shipping_cost))
    total = discount * n + ship_price
    return total

print(total_books(60))

left_house = (6 * 3600 + 52 * 60)  # seconds
mile_pace = (8 * 60 + 15) * 2  # seconds/mile; ran two miles slow
three_miles_pace = (7 * 60 + 12) * 3  # seconds/mile; three miles fast

breakfast_time_hours = (left_house + mile_pace + three_miles_pace) / 3600  # final time in hours
mins_in_hour = (left_house + mile_pace + three_miles_pace) // 3600  # Remainder = minutes
breakfast_time_min = (breakfast_time_hours - mins_in_hour) * 60

print(str(int(breakfast_time_hours)) + ':' + str(int(breakfast_time_min)))


# Exercise 1

fin = open('words.txt')
for line in fin:
    word = line.strip()
    if len(word) > 20:
        print(word)


# Exercise 2

def has_no_e(n):
    """
    Returns True if the given word doesn’t have the letter 'e' in it.

    Parameters:
    - n (str): Input word.

    Returns:
    - bool: True if 'e' is not present, False otherwise.
    """
    for l in n:
        if 'e' not in l:
            return True
        else:
            return False

##print(has_no_e('string'))

def word_no_e():
    """
    Reads words.txt and prints only the words that have no 'e'.
    Computes the percentage of words in the list that have no 'e'.
    """
    fin = open('words.txt')
    word = line.strip()
    count = 0
    total = 0
    for i in fin:
        if 'e' not in i:
            count += 1
        else:
            total += 1
    total_actual = total + count
    print("Percent 'e' not present:" + str((count / (total_actual)) * 100))

##word_no_e()

# Exercise 3

def avoids(word, string):
    """
    Takes a word and a string of forbidden letters,
    and returns True if the word doesn’t use any of the forbidden letters.

    Parameters:
    - word (str): Input word.
    - string (str): String of forbidden letters.

    Returns:
    - bool: True if none of the forbidden letters are present, False otherwise.
    """
    for val in word:
        if val in string:
            return False
        else:
            return True

##print(avoids('happy', 'q'))
fin = input("Enter a string of forbidden letters: ")

def let(word):
    """
    Prompts the user to enter a string of forbidden letters and
    then prints the number of words that don’t contain any of them.

    Parameters:
    - word (str): Input word.
    """
    sum = 0
    for w in fin:
        total = avoids(word, w.strip())
        if total == True:
            sum += 1
            print(w.strip())
    return sum

##print(avoids('ok', 'good'))
##print("The number of words that don't contain any of the string: " + let('good'))

# Exercise 4

def uses_only(word, string):
    """
    Takes a word and a string of letters,
    and returns True if the word contains only letters in the list.

    Parameters:
    - word (str): Input word.
    - string (str): String of accepted letters.

    Returns:
    - bool: True if the word contains only accepted letters, False otherwise.
    """
    for r in word:
        if r in string:
            return True
        else:
            return False

list = open("words.txt")

def search():
    """
    Input a string of accepted letters and prints words that have those letters.
    """
    count = 0
    g = input('Input a string of accepted letters: ')
    for i in list:
        word = i.strip()
        if uses_only(word, g):
            print(word)
            count += 1
        print(count)

##print(search())

# Exercise 5

list = open("words.txt")

def uses_all(word, string):
    """
    Takes a word and a string of required letters,
    and returns True if the word uses all the required letters at least once.

    Parameters:
    - word (str): Input word.
    - string (str): String of required letters.

    Returns:
    - bool: True if the word uses all required letters, False otherwise.
    """
    for a in string:
        if a in word:
            return True
        else:
            return False

def include():
    """
    Input a string of accepted letters and prints words that have all those letters.
    """
    letters = 0
    inc = input("Input a string of accepted letters: ")
    inc = inc.lower()

    for f in list:
        word = f.strip()
        if uses_all(word, inc):
            print(word)
            letters += 1
    return letters

##print(include())

# Exercise 6

def is_abecedarian(word):
    """
    Returns True if the letters in a word appear in alphabetical order.

    Parameters:
    - word (str): Input word.

    Returns:
    - bool: True if the letters are in alphabetical order, False otherwise.
    """
    one = word[0]
    two = word[1]
    Z = 1

    while z == two:
        return False
        if one == two:
            Z += 1
            two = word[Z]
    return True

list = open("words.txt")

def count():
    """
    Counts how many words are abecedarian.
    """
    t_count = 0
    for d in list:
        if is_abecedarian(word):
            print(word)
            t_count += 1
    return t_count

##print(count())

# Exercise 7

def is_palindrome(num):
    """
    Takes in a word and checks if it is a palindrome.

    Parameters:
    - num (str): Input word.

    Returns:
    - bool: True if the word is a palindrome, False otherwise.
    """
    return str(num) == str(num)[::-1]

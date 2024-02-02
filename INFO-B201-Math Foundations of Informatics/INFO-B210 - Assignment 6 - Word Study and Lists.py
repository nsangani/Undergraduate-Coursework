
# Neel Sangani
# Assignment 6 - Python Practice

# Exercise 7

def is_triple_double(word):
    """
    Tests if a word contains three consecutive double letters.

    Parameters:
    - word (str): Word to be tested.

    Returns:
    bool: True if the word contains three consecutive double letters, False otherwise.
    """
    i = 0
    count = 0
    while i < len(word)-1:
        if word[i] == word[i+1]:
            count = count + 1
            if count == 3:
                return True
            i = i + 2
        else:
            count = 0
            i = i + 1
    return False

def find_triple_double():
    """
    Reads a word list and prints words with triple double letters.

    Returns:
    None
    """
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if is_triple_double(word):
            print(word)

print('Here are all the words in the list that have')
print('three consecutive double letters.')
find_triple_double()
print('\n')

# Exercise 8

def has_palindrome(i, start, length):
    """
    Returns True if the integer i, when written as a string,
    contains a palindrome with length (length), starting at index (start).

    Parameters:
    - i (int): Integer to be checked.
    - start (int): Starting index of the palindrome.
    - length (int): Length of the palindrome.

    Returns:
    bool: True if the palindrome is found, False otherwise.
    """
    s = str(i)[start:start+length]
    return s[::-1] == s

def check(i):
    """
    Checks whether the integer (i) has the properties described
    in the puzzler.

    Parameters:
    - i (int): Integer to be checked.

    Returns:
    bool: True if the properties are satisfied, False otherwise.
    """
    return (has_palindrome(i, 2, 4) and
            has_palindrome(i+1, 1, 5) and
            has_palindrome(i+2, 1, 4) and
            has_palindrome(i+3, 0, 6))

def check_all():
    """
    Enumerates the six-digit numbers and prints any that satisfy the
    requirements of the puzzler.

    Returns:
    None
    """
    i = 100000
    while i <= 999996:
        if check(i):
            print(i)
        i = i + 1

print('The following are the possible odometer readings:')
check_all()

# Exercise 9

def str_fill(i, length):
    """
    Return the integer (i) written as a string with at least (length) digits.

    Parameters:
    - i (int): Integer to be converted to a string.
    - length (int): Minimum length of the resulting string.

    Returns:
    str: String representation of the integer with at least the specified length.
    """
    return str(i).zfill(length)

def are_reversed(i, j):
    """
    Return True if the integers i and j, written as strings,
    are the reverse of each other.

    Parameters:
    - i (int): First integer to be compared.
    - j (int): Second integer to be compared.

    Returns:
    bool: True if the integers are reversed, False otherwise.
    """
    return str_fill(i, 2) == str_fill(j, 2)[::-1]

def num_instances(diff, flag=False):
    """
    Returns the number of times the mother and daughter have
    palindromic ages in their lives, given the difference in age.
    If flag is True, prints the details.

    Parameters:
    - diff (int): Age difference between mother and daughter.
    - flag (bool, optional): If True, print the details. Defaults to False.

    Returns:
    int: Number of instances where ages are palindromic.
    """
    daughter = 0
    count = 0
    while True:
        mother = daughter + diff
        if are_reversed(daughter, mother) or are_reversed(daughter, mother + 1):
            count = count + 1
            if flag:
                print(daughter, mother)
        if mother > 120:
            break
        daughter = daughter + 1
    return count

def check_diffs():
    """
    Enumerates the possible differences in age between mother
    and daughter, and for each difference, count the number of times
    over their lives they will have ages that are the reverse of
    each other.

    Returns:
    None
    """
    diff = 10
    while diff < 70:
        n = num_instances(diff)
        if n > 0:
            print(diff, n)
        diff = diff + 1

print('diff  #instances')
check_diffs()

print('daughter  mother')
num_instances(18, True)

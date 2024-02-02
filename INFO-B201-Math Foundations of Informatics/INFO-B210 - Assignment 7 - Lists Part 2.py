
# Neel Sangani
# Assignment 7 - Lists

# Exercise 1

def nested_sum(t):
    """Takes a list of lists of integers and adds up
    the elements from all of the nested lists."""
    total = 0
    for a in t: 
        for b in a:
            total += b
    return total

t = [[1, 2], [3], [4, 5, 6]]
# print(nested_sum(t))

# Exercise 2

def cum_sum(num):
    """Takes a list of numbers and returns the cumulative sum;
    that is, a new list where the ith element is the sum of the
    first i+1 elements from the original list."""
    total = 0
    cumsum = []  # Empty list
    for c in num:
        total += c  # Keep adding the total to the next value -> cumulative sum
        cumsum.append(total)  # Adding total to the cumsum list
    return cumsum

t = [1, 2, 3]
# print(cum_sum(t))

# Exercise 3

def chop(t):
    """Takes a list, modifies it by removing the first and last elements, and returns None."""
    del t[0]  # Deletes the Zeroth index value
    del t[len(t)-1]  # Targets the last index by subtracting the len by 1 since the indexing starts from zero

t = [1, 2, 3, 4]
# chop(t)
# print(t)  # Gives the chopped list

# Exercise 4

def is_sorted(t):
    """Takes a list as a parameter and returns True if the list is sorted in ascending order
    and False otherwise."""
    for i in range(len(t)-1):
        if t[i+1] < t[i]:  # Using relational operators we can check whether index [i+1] is less than [i] or not
            return False
    return True

# print(is_sorted([1, 2, 2]))

# Exercise 5

file = open('words.txt')

def build_list():
    """Reads the file words.txt and builds a list with one element per word."""
    word_list = []
    for line in file:
        word = line.strip()  # Clears the empty spaces around the sentence
        word_list.append(word)  # Makes a list out of the sentence in word_list
    return word_list

# print(build_list())

# Exercise 6

def rev_pairs(word_list):
    for word in word_list:
        if word[::-1] in word_list:
            print(word, word[::-1])

            
# rev_pairs(build_list())  # Loops through the word file and looks for reverse pairs

































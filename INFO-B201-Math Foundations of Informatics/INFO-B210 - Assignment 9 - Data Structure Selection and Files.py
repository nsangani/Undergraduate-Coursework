
# Neel Sangani
# Assignment 9 - Files

# Chapter 14 Exercises 9

# Exercise 1

def sed(pattern, replacement, fopen, fclose):
    """Takes as arguments a pattern string, a replacement string,
    and two filenames; it should read the first file and
    write the contents into the second file (creating it if necessary).
    If the pattern string appears anywhere in the file,
    it should be replaced with the replacement string.

    Inputs:
    pattern: string
    replacement: string
    fopen: string (input filename)
    fclose: string (output filename)

    Output:
    None (writes to the specified output file)
    """

    fname = open(fopen)

    fwrite = open(fclose, 'w')

    for i in fname:
        if pattern in i:
            var = i.replace(pattern, replacement)
            fwrite.write(var)
        else:
            fwrite.write(i)

# Example usage:
# sed('George', 'Dave', 'sample.txt', 'sample_1.txt')

# Exercise 2

"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

import anagram_sets
import shelve
import sys

def store_anagrams(filename, anagram_map):
    """Create a DBM database and store the anagram
    dictionary in the database.

    Inputs:
    filename: string (output filename)
    anagram_map: dictionary

    Output:
    None (creates a DBM database)
    """
    
    shelf = shelve.open(filename, 'c')

    for word, list_word in anagram_map.items():
        shelf[word] = list_word

    shelf.close()


def read_anagrams(filename, word):
    """Look up a word and return a list of its anagrams.

    Inputs:
    filename: string (input filename)
    word: string

    Output:
    list of strings (anagrams of the given word)
    """
    
    shelf = shelve.open(filename)
    sig = signature(word)
    try:
        return shelf[sig]
    except KeyError:
        return []

def main(script, command='make_db'):
    if command == 'make_db':
        anagram_map = find_anagrams(make_wordlist("words.txt"))
        store_anagrams('anagrams.db', anagram_map)
    else:
        print(read_anagrams('anagrams.db', command))

def make_wordlist(file):
    """Reads a word list from a file.

    Input:
    file: string (input filename)

    Output:
    list of strings
    """
    result = []
    wordlist = open(file)
    for line in wordlist:
        word = line.strip()
        result += [word]  # Creates a list - result
    return result

list_words = make_wordlist("words.txt")

def find_anagrams(list_words):
    """Prints all the sets of words that are anagrams.

    Input:
    list_words: list of strings

    Output:
    list of lists of strings
    """
    d = {}  # Dict.
    for item in list_words:
        letters = []
        for letter in item:
            letters += letter
        r = tuple(sorted(letters))  # Alphabetical
        if r in d:
            d[r].append(item) 
        else:
            d[r] = [item]

    anagrams = []
    for item in d.values():
        if len(item) > 1:
            anagrams += [item]
    sorted_anagrams = sorted(anagrams, key=len, reverse=True)
    return sorted_anagrams    

def signature(s):
    """Returns the signature of this string.

    Signature is a string that contains all of the letters in order.

    Input:
    s: string

    Output:
    string
    """
    # TODO: rewrite using sorted()
    t = list(s)
    t.sort()
    t = ''.join(t)
    return t




        

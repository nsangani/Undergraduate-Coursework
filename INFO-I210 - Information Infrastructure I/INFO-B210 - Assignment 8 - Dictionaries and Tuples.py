##Chapter 11 Exercises

##Exercise 1

fin = open('words.txt')
for line in fin:
    word = line.strip() #reads the words in words.txt
    
d = dict()
for i in word:
    if i not in d:
        d[i] = 1 #assigns an index value 1 if the word is not present
    else:
        d[i] = d[i] + 1 #increase the count by one if the work is in the dictionary
print(d)

##Chapter 12 Exercises

##Exercise 1

def make_dict(x):
    """Takes and string and check with the dictionary. Then it
    either makes a new dictionary set or append the counter to the existing one"""
    dictionary = {} 
    for letter in x:
        dictionary[letter] = dictionary.get(letter, 0) + 1 
    return dictionary


def most_frequent(text):
    """ Takes a string and prints the letters in decreasing order of frequency"""
    letters = [letter.lower() for letter in text if letter.isalpha()] #lowers the input if it is alphabets only
    dictionary = make_dict(letters) #lowered case letter is referred to make_dict function to check its existence
    result = []
    for key in dictionary:
        result.append((dictionary[key], key))
    result.sort(reverse=True) #Flips the order
    for count, letter in result:
        print (letter, count)

print(most_frequent(text))

##Exercise 2

#1

def make_wordlist(file):
    """reads a word list from a file"""
    result = []
    wordlist = open(file)
    for line in wordlist:
        word = line.strip()
        result += [word]
    return result

wordlist = make_wordlist("words.txt")

def find_anagrams(list_words):
    """prints all the sets of words that are anagrams"""
    d = {}
    for item in list_words:
        letters = []
        for letter in item:
            letters += letter
        r = tuple(sorted(letters)) #alphabetical
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

#2

def find_bingos(anagrams):
    """Filters mydict for keys of length 8. Sorts a list of the values
     (lists) and sorts by length in reverse order"""
    candidates = [anagrams[key] for key in anagrams if len(key) == 8]
    candidates.sort(key=len, reverse=True)

    print ("Top Bingos:")
    for i in range(0, 5):
        fp = ''.join(sorted(candidates[i][0]))
        print(((i + 1), len(candidates[i]), fp), candidates[i])

print(find_bingos(anagrams))

##Non-chapter exercise

alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
 
reverse_alphabet = list(reversed(alphabet))

code_dictionary = dict(zip(alphabet, reverse_alphabet)) #Creating a dictionary {'A':'Z',...}

def atbash_cipher(code):
    characters = list(code.upper())

    result = ""

    for c in characters:
        if c in code_dictionary:
            result += code_dictionary.get(c)  #looks for c in index[1] of the dictionary and
                                              # saves index[2] of that set to result
    return result

print(atbash_cipher('NLIMRMT'))


##Exercise 4  

def str_fill(i, len):
    """return the integer (i) written as a string with at least
    (len) digits"""
    return str(i).zfill(len) 


def are_reversed(i, j):
    """ return True if the integers i and j, written as strings,
    are the reverse of each other"""
    return str_fill(i,2) == str_fill(j,2)[::-1] #flips and check whether same or not


def num_instances(diff, flag=False): #initial flag as false 
    """returns the number of times the mother and daughter have
    pallindromic ages in their lives, given the difference in age.
    If flag==True, prints the details."""
    daughter = 0
    count = 0
    while True:
        mother = daughter + diff
        if are_reversed(daughter, mother) or are_reversed(daughter, mother+1): #loops througgh previous def function to check for the reverse combo
            count = count + 1 #if there is then append
            if flag:
                print (daughter, mother)
        if mother > 120: #age limit of course
            break
        daughter = daughter + 1
    return count
    

def check_diffs():
    """enumerate the possible differences in age between mother
    and daughter, and for each difference, count the number of times
    over their lives they will have ages that are the reverse of
    each other."""
    diff = 10 #pre-given
    while diff < 70: 
        n = num_instances(diff) #loops through num_instance to get count
        if n > 0:
            print (diff, n)
        diff = diff + 1

print ('diff  #instances')
check_diffs()


print ('daughter  mother')
num_instances(18, True)






















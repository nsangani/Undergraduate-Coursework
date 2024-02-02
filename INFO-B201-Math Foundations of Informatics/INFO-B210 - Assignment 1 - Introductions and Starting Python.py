
# Neel Sangani
# Assignment 1 - Calculate Change

def convertTuple(tup): 
    """
    Function to convert a tuple to a string.

    Parameters:
    - tup (tuple): Input tuple to be converted.

    Returns:
    - str: Converted string.
    """
    str =  ''.join(tup) 
    return str

def change(x):
    """
    Function to convert a given amount into dollars, quarters, dimes, nickels, and pennies.

    Parameters:
    - x (float): Input amount in dollars.

    Returns:
    - str: String representation of the converted amounts.
    
    Example:
    >>> change(7.52)
    '7 dollars, 2 quarters, 2 nickels, and 2 pennies.'
    """
    dollars = 0      # 100 cents
    quarter = 0      # 25 cents
    dimes   = 0      # 10 cents
    nickels = 0      # 5 cents
    pennies = 0      # 1 cent
    x = x * 100
    if x >= 100:
        dollars = x // 100
        x = x - dollars * 100
    if x >= 25:
        quarter = x // 25
        x = x - quarter * 25
    if x >= 10:
        dimes = x // 10
        x = x - dimes * 10
    if x >= 5:
        nickels = x // 5
        x = x - nickels * 5
    else:
        pennies = x // 1
    return convertTuple((str(int(dollars)), ' dollars,', str(int(quarter)), ' quarters,',
            str(int(dimes)), ' dimes,', str(int(nickels)), ' nickels, and',
            str(int(pennies)), ' and pennies.'))

x = 7.52
print(change(x))

def change(x):
    """
    Revised function to convert a given amount into dollars, quarters, dimes, nickels, and pennies using while loops.

    Parameters:
    - x (float): Input amount in dollars.

    Returns:
    - str: String representation of the converted amounts.
    
    Example:
    >>> change(7.52)
    '7 dollars, 2 quarters, 2 nickels, and 2 pennies.'
    """
    dollars = 0      # 100 cents
    quarter = 0      # 25 cents
    dimes   = 0      # 10 cents
    nickels = 0      # 5 cents
    pennies = 0      # 1 cent
    change = x * 100
    while change > 100:
        change = change - 100
        dollars = dollars + 1
    while change >= 25:
        change = change - 25
        quarter = quarter + 1
    while change >= 10:
        change = change - 10
        dimes = dimes + 1
    while change >= 5:
        change = change - 5
        nickels = nickels + 1
    while change >= 1:
        change = change - 1
        pennies = pennies + 1
    return convertTuple((str(dollars), ' dollars,', str(quarter), ' quarters,',
            str(dimes), ' dimes,', str(nickels), ' nickels, and',
            str(pennies), ' pennies.'))

print(change(x))

sandwich = 3.48
def purchase_sandwich(y):
    """
    Function to simulate a sandwich purchase.

    Parameters:
    - y (float): Amount of money available.

    Returns:
    - str: String representation of the change after purchasing a sandwich, if enough money is available.
           Prints 'Not enough money bro' if the amount is insufficient.

    Example:
    >>> purchase_sandwich(5.0)
    '1 dollar, 2 quarters, 1 nickel, and 2 pennies.'
    """
    if y > sandwich:
        return change(y - sandwich)
    else:
        print('Not enough money bro')

y = x
purchase_sandwich(y)

def recursive_sandwich(z):
    """
    Function to simulate recursive sandwich purchases.

    Parameters:
    - z (float): Total amount of money available.

    Example:
    >>> recursive_sandwich(45.89)
    'Number of sandwiches: 13 and Money left: 4 dollars, 2 quarters, 1 dime, 1 nickel, and 4 pennies.'
    """
    t_sandwich = 0
    while z > sandwich:
        purchase_sandwich(z)
        z = z - sandwich
        t_sandwich = t_sandwich + 1
    print ('Number of sandwiches: '+ convertTuple(str(t_sandwich)), 'and Money left: '+ str(change(z)))

z = float(input('How much money you got to buy sandwiches (Ex: 45.89)? '))
recursive_sandwich(z)











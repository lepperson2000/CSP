def food_id(food):
    '''Returns categorization of food
    
    food is a string
    returns a string of categories
    '''
    # The data
    fruits = ['apple', 'banana', 'orange']
    citrus = ['orange']
    starchy = ['banana', 'potato']
    
    # Check the category and report
    if food in fruits:
        if food in citrus:
            return 'Citrus, Fruit'
        else:
            return 'Citrus, Fruit'
    else:
        if food in starchy:
            return 'Starchy, NOT Fruit'
        else:
            return 'NOT Starchy, NOT Fruit'

def food_id_test():
    ''' Unit test for food_id
    returns True if good, returns False and prints error if not good
    '''
    works = True
    if food_id('orange') != 'Citrus, Fruit':
        works = False
        print ('orange bug in food id()')
    if food_id('banana') != 'NOT Citrus, Fruit':
        works = False
        print('banana bug in food_id()')
    #Add tests so that all lines of code are visited during test
    
    if works:
        print('food_id passed all tests')
    return works
    
def f(x):
    if int(n)==n:
        works = True
    if n%2==0
        works True
    if n%3==0
        works = True
    print('n is a multiple of 6')
    
    
def f(x):
    if int(n) >= 0
        works = False
        print ('n is not an integer')
    if n%2 != 0
        works = False
        print ('n is odd')
    if n%3 != 0
        works = False
        print('n is even')
        
    
    
from __future__ import print_function #must be first in file
import random

def guess_once():
    secret = random.randint(1,4)
    print('I have a number between 1 and 4 inclusive')
    guess = int(raw_input('Guess: '))
    if guess != secret:
        print('Wrong, my number is ', secret, '.', sep='')
    else:
        print('Right, my number is', guess, end-'!\n')
        
        
        
from __future__ import print_function
import random

def quiz_decimal(low, high):
    print('Type a number between 4 and 4.1')
    guess = int(raw_input('Guess: '))
    if guess != quiz_decimal:
        print('No, number is less/greater than 4.1')
    else:
        print('No, number is greater than 4.1')
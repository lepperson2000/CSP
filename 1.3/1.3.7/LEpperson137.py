import matplotlib.pyplot as plt
import random


def days():
    '''function explanation: the print will be of the 'MTWRFSS' in front of
    'day' and the print will include the 5-7 days of September
    '''
    for day in 'MTWRFSS':
        print(day + 'day')
    for day in range(5,8):
        print('It is the ' + str(day) + 'th of September')
        
        

plt.ion() # sets "interactive on": figures redrawn when updated

def picks():
    a = [] # make an empty list
    
    a += [random.choice([1,3,10])]
    
    plt.hist(a)
    plt.show()
    
           
def roll_hundred_pair():
    b = []
    
    b += [random.choice([2,4,6])]
    
    plt.hist(b)
    plt.show()
    
    
def dice(n):
    number = range(2-12)
    number += [random.choice(range(2,12))]
    return dice(n)


def hangman_display(guessed, secret):
    
    letter = range(1,26)
    letter += [hangman_display(range(1,26))]
    return hangman_display(guessed, secret)
    
    
def matches(ticket, winners):
  
  ticket = list[11,12,13,14,15]
  winners = list[3,8,12,13,17]
  
  for ticket in winners:
      print(matches)
      
def report(guess, secret):
    
    color = range(1,4)
    color += [report(range(1,4))]
    return report(guess, secret)
from __future__ import print_function #use Python 3.0 printing

def age_limit_output(age):
    ''' Step 6a if-else example'''
    AGE_LIMIT = 13      #convention: use CAPS for constants
    if age< AGE_LIMIT:
        print(age, 'is below the age limit,')
    else:
        print(age, 'is old enough.')
    print('Minimm age is', AGE_LIMIT)
    
    
def report_grade(percent):
    ''' Step 6b if-else'''
    PERCENT_MASTERY = 80
    if percent<PERCENT_MASTERY:
        print (percent, 'NOT MASTERY')
    else:
        print(percent, 'MASTERY')
    print('PERCENT MASTERY IS GREATER THAN OR EQUAL TO 80')
    
    
def vowel(letter):
        vowels = 'aeiouAEIOU'
        if letter in vowels:
            return True
        else:
            return False
    # should check len(letter)==1
    

def letter_in_word(guess, word):
    guess = word
    if guess in word:
        return True
    else:
        return False
        
        
def hint(color, secret):
    ''' Includes a string that represents a color and a list of strings that represents a sequence of colors'''
    if color in secret:
        return True
    else:
        return False
        
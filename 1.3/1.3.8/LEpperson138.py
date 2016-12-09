from __future__ import print_function
import random



def validate():
    guess = 'a' #initialization with a bad guess
    answer = 'hangman word'
    while guess not in answer:
        guess = raw_input( 'Name a letter in \ ''+answer+\': ')
    print('Thank you!')
    
    
def guess_winner(players=('Amy', 'Bill', 'Cathy', 'Dale')):
        ''' This function guesses who will be the winner out of
        the four given names
        
        The arguments include 'Amy', 'Bill', 'Cathy', and 'Dale'.
        The code will decide who is the winner based on a guesss.
        '''
        
        winner = random.choice(players)
        
        ####
        # Now the code will begin to choose the winner
        ####
        
        print('Guess which of these people won the lottery: ',end='')
        for p in players[:len(players)-1]: # The code will tell who has
        # won the game and will say and will print "Guess which of
        # these people won the lottery: [Name], end.
        
            print(p,', ', end='')
        print(players[len(players)-1]) # This line of code will print
        # 'p, [Name of winner] minus the 's' in 'players'.
        
        
        ####
        # The following section of code will allow the coder to guess
        # a number which will, in turn, print 'Guess again!'.
        # If the user guesses '+= 1' then the code will print
        # 'You guessed in', guesses, 'guesses!' and will return guesses.
        ####
        
        guesses = 1
        while raw_input() != winner:
            print('Guess again!')
            guesses += 1
        print('You guessed in', guesses, 'guesses!')
        return guesses
        
        
        
def goguess():
        
    print('I have a number between 1 and 20 inclusive.')
    
    number = goguess
    
    while number in goguess() == goguess:
        print('number is too high' or 'number is too low')
        
    while number in goguess() != goguess:
        print ('Right! My number is !' 'You guessed in ', number, 'guesses!')
# -*- coding:cp1252 -*-
def add_tip(total, tip_percent):
    '''Return the total amount including tip
    '''
    tip = tip_percent*total
    return total + tip
    
    
def hyp(leg1, leg2):
    ''' Return the length of the hypotenuse of a right triangle
    '''
    c = (leg1**2, leg2**2) **0.5
    return c
    
    
def mean(a,b,c):
    ''' Return the mean of the three numbers
    '''
    mean = (a+b+c) /3
    return mean


def perimeter(base, height):
    ''' Return the perimeter of the rectangle with the side lengths base and height
    '''
    perimeter = (base+11, height-4)
    return perimeter
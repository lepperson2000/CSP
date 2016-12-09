def how_eligible(essay):
    ''' Returns 0 to 4 '''
    count = 0
    if '?' in essay:
        count = count + 1
    if '"' in essay:
        count = count + 1
    if ',' in essay:
        count = count + 1
    if '!' in essay:
        count = count + 1
        
    return count
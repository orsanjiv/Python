import random,os
def random_line(fname):    
    lines = open(fname).read().splitlines()    
    return random.choice(lines)
#dir location for the txt file
os.chdir('C:/Users/SANJIV/Documents/GitHub/Python/Worksheets/worksheet11/textFile')
print('\nRandom line is',random_line('words.txt'))
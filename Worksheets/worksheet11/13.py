import random,os
def random_line(fname):    
    lines = open(fname).read().splitlines()    
    return random.choice(lines)
#dir location for the txt file
os.chdir('C:/Users/SANJIV/Documents/GitHub/Python/Worksheets/worksheet11/textFile')
print('\nRandom line is',random_line('words.txt'))


# open(fname) opens the file whose name is specified in the variable fname.
# .read() reads the content of the file and returns it as a string.
# .splitlines() splits the string into a list of lines, removing the newline character (\n) at the end of each line.
#random.choice() selects a random item from a list.
# The lines variable contains a list of lines that were read from a text file earlier in the program.
# random.choice(lines) selects a random line from the list of lines.
# The return statement returns the randomly selected line as the output of the random_line() function.
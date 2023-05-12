import string, os

os.chdir('C:/Users/SANJIV/Documents/GitHub/Python/Worksheets/worksheet11/textFile')
for letter in string.ascii_uppercase:   
  with open(letter + ".txt", "w") as f:       
    f.writelines(letter)

# "with" statement ensure that the file should be closed after execution
# block of code
# "writelines" used to write a list of strings to a file
# "as f" part of the with statement is used to create a file object and assign it to the variable f
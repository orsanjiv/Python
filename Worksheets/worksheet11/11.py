import string, os

os.chdir('C:/Users/SANJIV/Documents/GitHub/Python/Worksheets/worksheet11/textFile')
for letter in string.ascii_uppercase:   
  with open(letter + ".txt", "w") as f:       
    f.writelines(letter)
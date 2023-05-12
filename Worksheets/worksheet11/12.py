import string,os
def letters_file_line(n):   
 with open("words.txt", "w") as f:       
    alphabet = string.ascii_uppercase       
    letters = [alphabet[i:i + n] + "\n" for i in range(0, len(alphabet),)]          
    f.writelines(letters)

#dir location for the txt file
os.chdir('C:/Users/SANJIV/Documents/GitHub/Python/Worksheets/worksheet11/textFile')
letters_file_line(4)
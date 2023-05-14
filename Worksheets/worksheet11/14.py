import os

os.chdir('C:/Users/SANJIV/Documents/GitHub/Python/Worksheets/worksheet11/textFile')

text = open("words.txt", "r")
d = dict()
for line in text:   
    # remove the whitespace 
    line = line.strip()
    # convert into small letter 
    line = line.lower()
    # split the line into words     
    words = line.split(" ")    
    for word in words:        
        if word in d:            
            d[word] = d[word] + 1        
        else:            
            d[word] = 1

for key in list(d.keys()):    
    print(key, ":", d[key])
def linear_search(List,Key):
 print(List)
 for i in range(len(List)): 
     if (List[i] == Key):
       return i 
 return -1
 
List=[]
size = int(input("Enter number of elements : ")) 
for i in range(0, size):
    element = int(input("Enter Element: "))
    List.append(element) 
Key = int(input("Enter Key to search : ")) 

result = linear_search(List,Key) 
if(result == -1):
 print("Element not found") 
else:
 print(Key,"is found at position:", result)

def binary_search(list1, Key):
  low = 0
  high = len(list1) - 1 
  while low <= high:
   mid = (high + low) // 2 
   if list1[mid] < Key:
    low = mid + 1 
   elif list1[mid] > Key: 
    high = mid - 1
   else:
    return mid 
  return -1

list1=[]
n = int(input("Enter number of elements : ")) 
for i in range(0, n):
    element = int(input("Enter Element: "))
    list1.append(element) 
Key = int(input("Enter Key to search : ")) 

result = binary_search(list1, Key) 
if(result == -1):
 print("Element not found")
else:
 print("Element is found")
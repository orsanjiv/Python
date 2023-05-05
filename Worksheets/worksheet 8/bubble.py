def bubbleSort(A):
  for num in range(len(A)-1,0,-1): 
    for i in range(num):
     if A[i]>A[i+1]:
      temp = A[i] 
      A[i] = A[i+1]
      A[i+1]=temp

A=[]
size = int(input("Enter number of elements : ")) 
for i in range(0, size):
    element = int(input("Enter Element: "))
    A.append(element) 

bubbleSort(A) 
print("Sorted List : ",A)

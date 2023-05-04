def selectionSort(List):
 for i in range(len(List)-1):
  minPos=i
  for j in range(i+1,len(List)):
    if List[j]<List[minPos]:
     minPos=j
  temp = List[i]
  List[i] = List[minPos] 
  List[minPos]=temp   

List=[]
size = int(input("Enter number of elements : ")) 
for i in range(0, size):
    element = int(input("Enter Element: "))
    List.append(element) 

selectionSort(List) 
print("Sorted List : ",List)

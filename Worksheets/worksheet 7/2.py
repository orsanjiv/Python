def removet(li):
     li = [num for num in li if num]
     return li
li = [(), ('0', '1', '2'), (), ('3', '4', '5', '6')]
print(removet(li))

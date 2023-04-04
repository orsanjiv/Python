lis = []
num =int(input("Enter number of elements: ")) 
for x in range(num):
    a = input(f"Enter {x + 1} element: ")
    lis.append(a)

del lis[5]
del lis[4]
del lis[0]

print(lis)

# write
obj1 =  open("demo.txt","w")
obj1.write("namaste duniya")
obj1.close()

# read
# obj1 =  open("demo.txt","r")
# z=obj1.read()
# print(z)

# append
obj1 = open("demo.txt","a")
obj1.write("\nnew namaste duniya")
obj1.close()

obj1 = open("demo.txt","r")
z = obj1.read()
print(z)



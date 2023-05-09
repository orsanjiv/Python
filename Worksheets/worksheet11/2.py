def fun():
    obj1 = open("demo.txt","w")
    for i in range(50):
        i = str(i)
        obj1.write(i)
        obj1.write(" ")
    obj1.close

fun()
obj2 = open("demo.txt","r")
z = obj2.read()
print(z);
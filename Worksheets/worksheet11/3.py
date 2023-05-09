def fun():
    obj1 = open("demo.txt","r")
    obj2 = open("demo2.txt","w")
    for i in obj1:
        obj2.write(i)
    obj2.close()

    obj2 = open("demo2.txt","r")
    text = obj2.read()

    print(text)
    obj1.close()
    obj2.close()

fun()    
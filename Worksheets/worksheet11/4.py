obj = open("test.txt","w+")
print(obj.write("hi!how are you"))
obj.seek(3)
print(obj.readline())
# obj.seek(0)
# obj.truncate()
# print(obj.readline)
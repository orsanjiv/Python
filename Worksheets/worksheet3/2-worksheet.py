def simp_multi(num):
    for i in range(1,11):
        print(num,"*",i,"=",i*num);


num=eval(input("Enter a number to print table:"))
print("Table of ",num,"is:")
simp_multi(num);

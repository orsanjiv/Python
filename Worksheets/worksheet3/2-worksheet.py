def simp_multi(num):
    for i in range(1,11):
        print(num,"*",i,"=",i*num);


num=eval(input("Enter a number to print table:"))
if (num>=2 and num<=20):
    print("Table of",num,"is:")
    simp_multi(num);
else:
    print("Please Enter Number Between 2 to 20");
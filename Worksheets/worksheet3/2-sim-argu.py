def simp_multi(num):
    for i in range(1,11):
        print(num,"*",i,"=",i*num)

def argu_multi(num,i):
    for i in range(1,11):
        print(num,"*",i,"=",i*num)

num=eval(input("Enter The Number:"));
i=1;
if(num>=2 and num<=20):   
 print("\nSimple Function:")
 simp_multi(num)

 print("\nFunction With Arguments:")
 argu_multi(num,i);
else:
   print("Please Enter Number between 2 to 20")         
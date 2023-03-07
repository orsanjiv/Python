# Simple Function
def simp_multi():
    print("Simple Function")
    num = eval(input("Enter The Number to Print Table:"))
    if(num>=2 and num<=20):
      for i in range(1,11):
        print(num,"*",i,"=",i*num) 

#function with arguments    
def argu_multi(num,i):
    for i in range(1,11):
        print(num,"*",i,"=",i*num)

#calling the simple function
simp_multi();

#taking input for parameterized function
num=eval(input("Enter The Number:"));
i=1;
if(num>=2 and num<=20):   
    print("\nFunction With Arguments:")
    #calling parameterized function
    argu_multi(num,i)
else:
   print("Please Enter Number between 2 to 20")         
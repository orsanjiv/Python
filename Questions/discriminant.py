def discri(a,b,c):
    discriment = b**2 - 4*a*c;
    return discriment  


num1 = eval(input("Enter value of A:"))
num2 = eval(input("Enter value of B:"))
num3 = eval(input("Enter value of C:"))


result = discri(num1,num2,num3)

if(result>0):
    print("The Equation has two Real Roots")
elif(result==0):
    print("The Equation has One Real Root")
elif(result<0):
    print("The Equation has two Complex Roots")  

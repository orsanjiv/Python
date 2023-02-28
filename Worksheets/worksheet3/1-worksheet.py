#Program to demonstrate the use of functions and passing different types of arguments in functions.
def add(num1,num2):
    sum=num1+num2
    return sum

a=eval(input("num1:"))
b=eval(input("num2:"))
sum = add(a,b);
print(sum);
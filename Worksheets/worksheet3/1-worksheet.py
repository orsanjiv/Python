#Program to demonstrate the use of functions and passing different types of arguments in functions.
# docstring must me there
#write a python program to calculate the area of 10 differet circle,given the PI=22/7 AND RADIUS OF CRICLES ENTERNED BY USER USING SIMPLE FUNCTION,PARAMETERIZED FUNCTION, RETURNED TYPE WITH FUNCTION AND RETURN TYPE WITH PARAMETERIZED FUNCTION
#Write a python program to print multiplication table from 2 to 20 ,where table values are entered by the user by using simple function,parameterized function,return with function and return type with parameterized function.


PI=3.14

def simple_area(radius):
    area = PI*radius*radius;
    print(area);

def area_para(PI,radius):
    area = PI*radius*radius;
    print(area)

def area_ret(radius):
    area = PI*radius*radius
    return area

def area_ret_para(PI,radius):
    area = PI*radius*radius
    return area

rad1 = float(input("Enter Rdius:"))
rad2 = float(input("Enter Rdius:"))
rad3 = float(input("Enter Rdius:"))
rad4 = float(input("Enter Rdius:"))
rad5 = float(input("Enter Rdius:"))
rad6 = float(input("Enter Rdius:"))
rad7 = float(input("Enter Rdius:"))
rad8 = float(input("Enter Rdius:"))
rad9 = float(input("Enter Rdius:"))
rad10 = float(input("Enter Rdius:"))
radius = [rad1,rad2,rad3,rad4,rad5,rad6,rad7,rad8,rad9,rad10]
print("Simple function")
for i in radius:
    simple_area(i);

print("\nfunction with arguments")
for i in radius:
    area_para(PI,i);

print("\nfunction with return type")
for i in radius:
    returnVar = area_ret(i);
    print(returnVar);

print("\nfunction with return type and arguments")
for i in radius:
    returnVar = area_ret_para(PI,i);
    print(returnVar);







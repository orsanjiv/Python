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
    return PI*radius*radius

def area_ret_para(PI,radius):
    return PI*radius*radius


radius =[1,2,3,4,5,6,7,8,9,10];
print("Simple function")
for i in radius:
    simple_area(i);






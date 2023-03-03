import math

def cal_dis(x1,x2,y1,y2):
    first = (x2-x1)**2;
    second = (y2-y1)**2;
    distance = math.sqrt(first + second);
    return distance

x1 = eval(input("Enter The x1 value:"))
x2 = eval(input("Enter The x2 value:"))
y1 = eval(input("Enter The y1 value:"))
y2 = eval(input("Enter The y2 value:"))

result=cal_dis(x1,x2,y1,y2);
print("The distance of two point is: {:.2f}".format(result))
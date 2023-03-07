PI = 3.14
def area_ret():
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
    print("\nRETURNED TYPE WITH FUNCTION ")
    areas=[]
    for i in radius:
        area = PI*i*i
        areas.append(area);
    return areas

def print_table_ret():
    table = area_ret()
    for i in range(10):
     print("{:.2f}".format(table[i]))

def area_ret_para(PI,radius):
    area = PI*radius*radius
    return area

print_table_ret()

print("\nRETURN TYPE WITH PARAMETERIZED FUNCTION")


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
for i in radius:
    returnVar = area_ret_para(PI,i);
    print("{:.2f}".format(returnVar));
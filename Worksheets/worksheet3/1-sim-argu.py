PI=3.14  

def simple_area():
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
        area = PI*i*i;
        print(area);

def area_para(PI,radius):
    area = PI*radius*radius;
    print(area)


simple_area();

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

print("Function with Argument")
for i in radius:
    area_para(PI,i)

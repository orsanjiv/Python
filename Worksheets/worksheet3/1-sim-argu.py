PI=3.14  
# Simple Function with no Arguments
def simple_area():
    rad1 = float(input("Enter Radius:"))
    rad2 = float(input("Enter Radius:"))
    rad3 = float(input("Enter Radius:"))
    rad4 = float(input("Enter Radius:"))
    rad5 = float(input("Enter Radius:"))
    rad6 = float(input("Enter Radius:"))
    rad7 = float(input("Enter Radius:"))
    rad8 = float(input("Enter Radius:"))
    rad9 = float(input("Enter Radius:"))
    rad10 = float(input("Enter Radius:"))
    radius = [rad1,rad2,rad3,rad4,rad5,rad6,rad7,rad8,rad9,rad10]
    print("Simple function")
    for i in radius:
        area = PI*i*i;
        print("{:.2f}".format(area))
        
# Function With Arguments
def area_para(PI,radius):
    area = PI*radius*radius;
    print("{:.2f}".format(area))


simple_area();

print("\nRadius for Function with Argument")
rad1 = float(input("Enter Radius:"))
rad2 = float(input("Enter Radius:"))
rad3 = float(input("Enter Radius:"))
rad4 = float(input("Enter Radius:"))
rad5 = float(input("Enter Radius:"))
rad6 = float(input("Enter Radius:"))
rad7 = float(input("Enter Radius:"))
rad8 = float(input("Enter Radius:"))
rad9 = float(input("Enter Radius:"))
rad10 = float(input("Enter Radius:"))
radius = [rad1,rad2,rad3,rad4,rad5,rad6,rad7,rad8,rad9,rad10]


for i in radius:
    area_para(PI,i)

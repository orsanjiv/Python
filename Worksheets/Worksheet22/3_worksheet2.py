num1 = eval(input("Enter Your First Number:"));
num2 = eval(input("Enter Your Second Number:"));
num3 = eval(input("Enter Your Third Number:"));

if num1>=num2 and num1>=num3:
    if num1==num2:
        print("num1 and num2 are equal and both are greater");
        exit();        
    if num1==num3:
        print("num1 and num3 are equal and both are greater");
        exit();
    print("Num 1 is Greater")

elif num2>=num1 and num2>=num3:
    if num2==num1:
        print("num2 and num1 are equal and both are greater");
        exit();    
    if num2==num3:
        print("num2 and num3 are equal and both are greater");
        exit();
    print("Num 2 is Greater")

elif num3>=num1 and num3>=num1:
    if num3==num1:
        print("num3 and num1 are equal and both are greater");
        exit();    
    if num3==num2:
        print("num3 and num2 are equal and both are greater");
        exit();
    print("Num 3 is Greater")
num1 = eval(input("Enter First Number:"))
num2 = eval(input("Enter second Number:"))
num3 = eval(input("Enter third Number:"))

largest = num1 if num1 > num2 and num1 > num3 else num2 if num2 > num3 else num3
print(largest)
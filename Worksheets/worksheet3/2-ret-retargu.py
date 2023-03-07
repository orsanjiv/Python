def generate_table():
    num = eval(input("Enter a number to print:"))
    table = []
    for i in range(1, 11):
      table.append(num*i)
    return table

def print_table():    
    table = generate_table()
    for i in range(10):
     print(table[0], "x", i+1, "=", table[i])

def generate_table_ret(num):
    table = []
    for i in range(1, 11):
      table.append(num*i)
    return table

def print_table_ret(num):
    table = generate_table_ret(num)
    for i in range(10):
     print(num, "x", i+1, "=", table[i]) 


# calling Function with return Type
print("Function with return Type")
print_table();

print("\nParameterized Function with return Type")
num=eval(input("Enter The Number:"));
# calling Parameterized Function with return Type
print_table_ret(num);


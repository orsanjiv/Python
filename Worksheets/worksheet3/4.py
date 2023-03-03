def simp_multi(num):
    for i in range(1,11):
        print(num,"*",i,"=",i*num)

def argu_multi(num,i):
    for i in range(10):
        print(num,"*",i,"=",i*num)


def generate_table(num):
    table = []
    for i in range(1, 11):
      table.append(num*i)
    return table

def print_table(num):
    table = generate_table(num)
    for i in range(10):
     print(num, "x", i+1, "=", table[i])

def generate_table_ret(num):
    table = []
    for i in range(1, 11):
      table.append(num*i)
    return table

def print_table_ret(num,i):
    table = generate_table_ret(num)
    for i in range(10):
     print(num, "x", i+1, "=", table[i])     


num=eval(input("Number likh:"));
i=1;
print("\nSimple Function:")
simp_multi(num)

print("\nFunction With Arguments:")
argu_multi(num,i);

print("\nReturn Type:")
print_table(num) 

print("\nReturn Type With Arguments:")
print_table_ret(num,i) 
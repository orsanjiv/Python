def simp_multi(num):
    for i in range(1,11):
        print(num,"*",i,"=",i*num)

def generate_table(num):
    table = []
    for i in range(1, 11):
      table.append(num*i)
    return table

num=eval(input("Number likh:"));
simp_multi(num);
pri=generate_table(num)
print(pri);
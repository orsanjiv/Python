def print_tables():
    for i in range(2, 21):
     for j in range(1, 11):
      print(i, "x", j, "=", i*j)
    # print()


print_tables()


def print_table(num):
    for i in range(1, 11):
     print(num, "x", i, "=", num*i)


for i in range(2, 21):
    print_table(i)
    # print()


def generate_table(num):
    table = []
    for i in range(1, 11):
      table.append(num*i)
    return table


def print_table(table):
    for i in range(10):
     print(num, "x", i+1, "=", table[i])


for num in range(2, 21):
    table = generate_table(num)
    print_table(table)
    # print()


def generate_table(num):
    table = []
    for i in range(1, 11):
     table.append(num*i)
    return table


def print_table(num):
    table = generate_table(num)
    for i in range(10):
     print(num, "x", i+1, "=", table[i])


# for i in range(2, 21):
#     print_table(i)
#     print()

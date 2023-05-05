my_list = [(1, 2, 3), (), (4, 5), (6,), (), (), (7, 8, 9)]
new_list = []
for tup in my_list:
 if tup:
  new_list.append(tup)
  
print(new_list)

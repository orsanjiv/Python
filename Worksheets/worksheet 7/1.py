my_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
for i in range(len(my_list)):
   temp_list = list(my_list[i])
   temp_list[-1] = 10
   my_list[i] = tuple(temp_list)
   
print(my_list)

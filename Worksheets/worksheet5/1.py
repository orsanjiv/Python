def get_last_element(tup):
    return tup[-1]
def sort_tuples(tuple_list):
    return sorted(tuple_list,key=get_last_element)



n = int(input("Enter the Number of Tuple:"))
tuple_list = []

for i in range(n):
    tup_str = input(f"Enter tuple {i+1}: ")
    tup_list = tup_str.split()
    tup = tuple(int(elem) for elem in tup_list)
    tuple_list.append(tup)

print("Initial list: ",tuple_list)
sorted_list = sort_tuples(tuple_list)
print("Sorted list:",sorted_list)
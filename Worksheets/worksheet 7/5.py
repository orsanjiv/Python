my_tuple = ((1, 2), (3, 4), (5, 6), (7, 8))
element = 5
for tup in my_tuple:
 if element in tup:
  print(f"The element {element} is present in the tuple ({tup})")
  break
 else:
  print(f"The element {element} is not present in any of the tuples")

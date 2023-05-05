def calculate_product(tup): 
 product = 1
 for num in tup: 
  product *= num
 return product
 
my_tuple = (1, 2, 3, 4, 5)

result = calculate_product(my_tuple) 
print(result)
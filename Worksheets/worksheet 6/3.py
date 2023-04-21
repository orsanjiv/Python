size = int(input("No. of elements:"))
d1 = {}

for i in range(size):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    d1[key] = value
    
print(d1);
keys1 = list(d1.keys())
values1 = list(d1.values())

print(keys1)
print(values1)


sorted_keys = sorted(keys1, reverse=True)
top3keys = sorted_keys[:3]

sorted_values = sorted(values1, reverse=True)
top3values = sorted_values[:3]

print("Top 3 values:", top3values)
print("Top 3 values:", top3keys)
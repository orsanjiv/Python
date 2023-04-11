size = int(input("No. of elements:"))
d1 = {}

for i in range(size):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    d1[key] = value

keys = list(d1.keys())
values = list(d1.values())

sorted_values = sorted(values, reverse=True)

top3values = sorted_values[:3]

top3keys = []

for key, value in d1.items():
 if value in top3values:
  top3keys.append(key)

sorted_keys = sorted(top3keys, reverse=True)
print("Top 3 keys:", sorted_keys)
print("Top 3 values:", top3values)

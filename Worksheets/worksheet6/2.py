dict = {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}

keys = list(dict.keys())
values = list(dict.values())

sorted_values = sorted(values, reverse=True)

top3values = sorted_values[:3]

top3keys = []

for key, value in dict.items():
 if value in top3values:
  top3keys.append(key)

sorted_keys = sorted(top3keys, reverse=True)
print("Top 3 keys:", sorted_keys)
print("Top 3 values:", top3values)

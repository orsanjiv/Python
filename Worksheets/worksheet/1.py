d1 = {'a': 100, 'b': 200, 'c': 300 ,'d':400}
d2 = {'a': 100, 'b': 200, 'c': 400}

for key in d2:
    if key in d1:
        d1[key] += d2[key]
    else:
        d1[key] = d2[key]

print(d1)
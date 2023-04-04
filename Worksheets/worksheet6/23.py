dict1 = {
    "Name":"SANJIV",
    "UID":"21BCS3478",
    "Section":611,
    "Group":"A"
}

key = list(dict1.keys())
values = list(dict1.values())

# print("keys:",key)
# print("Values:",values);

# adding new data to dictonary
dict1["branch"] = "CSE";
print(dict1)

# deleting data from dictonary
del dict1["branch"];
print(dict1);

# second dictonary for deltion of all elements from the dictonary
dict2 = {
    "Name":"Aman",
    "UID":"21BCS1236",
    "Section":810,
    "Group":"A"
}

del dict2
print(dict2)






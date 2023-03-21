def symmetric(string):
    n = len(string)
    for i in range(n//2):
        if string[i] != string[n-1-i]:
            return False
    return True

def palindrome(string):
    return symmetric(string)


string = str(input("Enter The String:"))
if symmetric(string):
    print(string,"is symmetric")
    if palindrome(string):
      print(string, "is a palindrome")
else:
    print(string, "is not a palindrome and Symmetic")




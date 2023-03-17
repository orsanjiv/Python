def is_symmetric(string):
    n = len(string)
    for i in range(n//2):
        if string[i] != string[n-1-i]:
            return False
    return True

def is_palindrome(string):
    return is_symmetric(string)

string = str(input("Enter The String:"))
# string1 = "racecar"
if is_symmetric(string):
    print(string,"is symmetric")
    if is_palindrome(string):
      print(string, "is a palindrome")

else:
    print(string, "is not a palindrome and Symmetic")

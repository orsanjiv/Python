s=str(input("Enter string:"))
if len(s)>2:
    if s.endswith("ing"):
        s+='ly'
    else:
        s+='ing'
    print(s)

if len(s)<3:
    print(s)
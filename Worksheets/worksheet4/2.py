def unCommon(A, B):
    A=A.split()
    B=B.split()
    x=[]
    for i in A:
        if i not in B:
            x.append(i)
    for i in B:
        if i not in A:
            x.append(i)
    return x

A = "Maths English science computer"
B = "datastructure computernetworks Maths English"
print(unCommon(A, B))




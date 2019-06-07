print("Enter string", end=" ")
s=input()
l=len(s)
c=[]
if(l>3):
    for i in range(0,3):
        c.append(s[i])
else:
    for i in range(l):
        c.append(s[i])
print(c)
    

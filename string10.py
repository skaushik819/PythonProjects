print("Enter string")
s=input()
l=len(s)
c=[]
k=l-1
for i in range(0,l):
    if(i%2==0):
        c.append(s[i])
    else:
        continue
print(c)
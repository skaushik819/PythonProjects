print("Enter string ")
s=input()
l=len(s)
c=[]
for i in range(0,l):
    c.append(s[i])
print("Enter the index position to be removed")
i=int(input())
del(c[i])
print(c)

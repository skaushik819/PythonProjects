print("Enter string :", end=" ")
s=input()
l=len(s)
k=l-2
c=[]
for i in range(0,2):
    c.append(s[k])
    k+=1
print(4*c)


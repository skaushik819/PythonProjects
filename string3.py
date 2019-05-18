s=input()
l=len(s)
k=l-2
c=[]
if(l<2):
    print("string length too short")
elif(l>3):
    for i in range(0,4):
        if(i<=1):
            c.append(s[i])
        else:
            c.append(s[k])
            k=k+1
            i=i+1
else:
    for h in range(0,5):
        if(h%2==0):
            c.append(s[0])
        else:
            c.append(s[1])
g=len(c)
for h in range(0,g):
    print(c[h])        
    

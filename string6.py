s=input()
l=len(s)
c=[]
if(l>=3):
    for i in range(0,l):
        c.append(s[i])
    if(s.endswith("ing")):
        c=c+list("ly")
    else:
        c=c+list("ing")
    j=len(c)
    print(c)
    
else:
    print("string length too short")

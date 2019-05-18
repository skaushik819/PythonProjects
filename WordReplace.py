s=input()
l=len(s)
c=[]
for i in range(0,l):
        if(i==0):
            c.append(s[i])
        else:
            if(s[i]==c[0]):
                c.append("$")
            else:
                c.append(s[i])

for i in range(0,l):
    print(c[i])
                                               

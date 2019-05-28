s1=input()
l1=len(s1)
s2=input()
l2=len(s2)
s3=" "
c=[]
k=1
le=l1+l2+1
for i in range(0,le):
    if(i==0):
        c.append(s2[0])
    elif(i<l1):
        c.append(s1[i])
    elif(i==l1):
        c.append(s3)
    elif(i==(l1+1)):
         c.append(s1[0])
    else:
         c.append(s2[k])
         k=k+1
for i in range(0,le):
    print(c[i])

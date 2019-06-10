l=[]
c=0
d={}
print("Enter number of values to be added :",end="")
n=int(input())
for i in range(0,n):
    print("Ener %s value:"%(i+1),end=" ")
    l.append(input())
for i in range(0,n):
    if(i==0):
        for j in range(i,n):
            if(l[i]==l[j]):
                c=1  
    else:
        br=1
        for k in range(0,i-1):
            if(l[i]==l[k]):
                br=0
        if(br==0):
            continue
        else:
            c+=1
            if(c==2):
                print("II repeated element is:",end="")
                print(l[i])

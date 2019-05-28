s=input()
l=len(s)
for i in range(0,l):
    if(i==0):
        count=0
        for j in range(i,l):
            if(s[i]==s[j]):
                count+=1
        print("%s :%s"%(s[i],count))
    else:
        br=1
        app=0
        for k in range(0,i-1):
            if(s[i]==s[k]):
                br=0
        if(br==0):
            continue
        else:
            for j in range(i,l):
                if(s[i]==s[j]):
                    app+=1
            print("%s:%s"%(s[i],app))
                

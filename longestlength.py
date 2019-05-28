c=[]
ch='y'
while(ch=='y'):
    print("Enter string")
    s=input()
    c.append(s)
    print("Enter your choice (y/n)")
    ch=input()
print(len(max(c)))

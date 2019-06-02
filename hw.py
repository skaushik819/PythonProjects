def write(a,b):
    import os
    os.mkdir("E:/python37/assignment")
    print("done")
    '''A is path & B is string'''
    f=open("%s"%(a),'w')
    f.write(b)
    f.close()
def append(a,b):
    f=open("%s"%(a),'a')
    f.write(b)
    f.close()
def read(a):
    f=open("%s"%(a),'r')
    print(f.read())
print("Enter your choice")
x='''1-Write on a file
2-Append a file
3-Read a file
4-Exit'''
print(x)
i=int(input())
if(i==1):
    print("Enter path")
    c=input()
    print("Enter string")
    v=input()
    write(c,v)
elif(i==2):
    print("Enter path")
    c=input()
    print("Enter string")
    v=input()
    append(c,v)
elif(i==3):
    print("Enter path")
    c=input()
    read(c)
else:
    exit()

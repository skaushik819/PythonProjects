import os
import pyperclip
def write(a):
    if(os.path.exists("assignment")):
        countt=1
    else:
        
        os.mkdir("E:/python37/assignment")
        print("done")
    '''A is path '''
    f=open("%s"%(a),'w')
    f.write(pyperclip.paste())
    f.close()
def append(a,b):
    f=open("%s"%(a),'a')
    f.write(pyperclip.paste())
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
    l=input()
    pyperclip.copy(l)
    write(c)
elif(i==2):
    print("Enter path")
    c=input()
    print("Enter string")
    v=input()
    ptyperclip.copy(v)
    append(c)
elif(i==3):
    print("Enter path")
    c=input()
    read(c)
else:
    exit()



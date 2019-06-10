l=[1,2,3,4,5]
l1=['a','b','c','d','e']
l.sort(reverse=True)
for a,b in zip(l,l1):
    print(str(a)+b,end=" ")

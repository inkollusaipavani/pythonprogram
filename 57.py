z,k=map(int,raw_input().split())
list=[int(i) for i in raw_input().split()]
if z in list:
    count=list.count(z)
    print count
elif k in list:
    count=list.count(k)
    print count
else:
    print (0)
    

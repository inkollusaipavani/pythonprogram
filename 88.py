s,p=map(int,raw_input().split())
if(s>p):
    min1=p
else:
    min1=p
while(1):
    if(min1%p==0 and min1%s==0):
        print(min1)
        break
    min1=min1+1

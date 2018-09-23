x,y=map(int,raw_input().split())
s=x*y
for z in range(s+1):
	if (z*z)==s:
		print "yes"
		break
else:
	print "no"

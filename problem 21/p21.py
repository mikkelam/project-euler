def properDiv(num):
	divs=0
	half= num/2
	for x in xrange(1,half+1):
		if num%x==0:
			divs +=x
	return divs

def amicable(cap):	
	amicables=[]
	for a in xrange(1,cap+1):
		b = properDiv(a)
		if a == properDiv(b):
			if a != b:
				if  a and b not in amicables:
					amicables.append(a)
					amicables.append(b)
	return amicables

print sum(amicable(10000))
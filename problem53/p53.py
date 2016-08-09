from math import factorial as f

greaters = 0
for n in xrange(23,101):
	for r in xrange(1,n+1):
		if f(n)/(f(r)*f(n-r)) > 1000000:
			greaters += 1
print greaters
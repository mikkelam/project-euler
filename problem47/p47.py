from pyprimes import primes_below
import time
import math

primes = list(primes_below(10000))

consecutives = []
num = 646
while len(consecutives)<4:
	p = 0
	dpf = set()
	tmp = num

	while (tmp != 1) and len(dpf) < 4 and p < len(primes)-1:
		if tmp % primes[p] == 0:
			tmp = tmp/primes[p]
			dpf.add(primes[p])
		else:
			p+=1
	if len(dpf) == 4:
		ok = True
		consecutives.append(num)
		for x in xrange(0,len(consecutives)-1):
			if consecutives[x] != consecutives[x+1]-1:
				ok = False
		if not ok:
			consecutives = [num]

		if len(consecutives)>=3:
			print consecutives


	num+=1



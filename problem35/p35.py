from pyprimes import isprime,primes_below
from time import sleep


def main():
	circprimes = []
	for x in primes_below(1000000):
		rots = rotations(x)
		ok = True
		for num in rots:
			if not isprime(num):
				ok = False
				break
		if ok:
			circprimes.append(x)
			print x
			# sleep(1)
	return len(circprimes)

def rotations(num):
	lst = [int(i) for i in str(num)]
	rots = [lst[:]]
	for x in xrange(1,len(lst)):
		lst.append(lst.pop(0))
		rots.append(lst[:])
	return [int(''.join(map(str, x))) for x in rots]

print main()
# from itertools import permutations
# print list(permutations([1,2,3], 3))
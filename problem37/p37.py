from pyprimes import isprime

def truncatable_prime(num):
	if not isprime(num):
		return False
	num = list(str(num))
	for limit in xrange(1, len(num)):
		n1 = int(''.join(map(str, num[limit:]))) 
		n2 = int(''.join(map(str, num[:-limit])))
		if not (isprime(n1) and isprime(n2)):
			return False
	return True

def main():
	candids = []
	for x in xrange(8,1000000):
		if truncatable_prime(x):
			candids.append(x)

	return candids, sum(candids)

print main()



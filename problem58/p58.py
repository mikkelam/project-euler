from pyprimes import isprime

def diags(sq,offset):
	return [sq[offset-1], sq[offset*2-1],sq[offset*3-1], sq[offset*4-1]]

def primecount(nums):
	p = 0
	np = 0
	for x in nums:
		if isprime(x):
			p+=1
		else:
			np+=1
	return p,np

prime_ratio = 100
r = 1
primes = 0
nums = 1
diagonals = []
start = 1
while prime_ratio>10:
	sq = range(start+1,start+(8*r)+1)
	diagonals = diags(sq,r*2)
	p, n = primecount(diagonals)
	primes += p
	nums += n+p
	prime_ratio = primes*100.0/nums
	r+=1
	start = sq[-1]


print (r-1)*2+1
















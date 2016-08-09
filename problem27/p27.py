from pyprimes import isprime

def quadratic_formula(n, a, b):
	return (n**2) + (a * n) + b

def main():
	winner = {'a': 0, 'b': 0, 'p': 0}
	for a in xrange(-999,999):
		for b in xrange(-999,999):
			n=0
			primes = 0
			while isprime(quadratic_formula(n, a, b)):
				primes += 1
				n += 1
			if primes > winner['p']:
				winner = {'a': a, 'b': b, 'p': primes}
	return winner

print main()
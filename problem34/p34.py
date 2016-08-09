from time import sleep
from math import factorial
def main():
	fits = []
	for x in xrange(3,1000000):
		concat = 0
		for lit in str(x):
			concat += factorial(int(lit))
		if x == concat:
			fits.append(concat)
			print x
	return sum(fits)

print main()
						
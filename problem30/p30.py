from time import sleep
def main():
	fits = []
	for x in xrange(2,1000000):
		concat = 0
		for lit in str(x):
			concat += int(lit)**5
		if x == concat:
			fits.append(concat)
	return sum(fits)

print main()
						
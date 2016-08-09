import math

def Tri(num):
	tries = []
	val=0

	for x in xrange(1,num):
		val = val + x
		tries.append(val)
	return tries
		
def Divisors(num):
	divisors = 0
	i = 1
	end = int(num**0.5)
	while i<end:
		if num%i==0:
			divisors+=1
		i+=1

	divisors *= 2

	return divisors

interval=100000

tries =[]
tries = Tri(interval)



for x in xrange(1,interval-1):
	div = Divisors(tries[x])
	great = 0
	if div > 500:
		print str(tries[x]) + " divisors:" + str(div)
		break

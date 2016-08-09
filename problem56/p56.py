def numsum(num):
	num = [int(x) for x in str(num)]
	return sum(num)
largest = 0
for a in xrange(0,100):
	for b in xrange(0,100):
		tmp = numsum(a**b)
		if tmp> largest:
			largest = tmp
print largest
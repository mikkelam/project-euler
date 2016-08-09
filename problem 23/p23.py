import time, math
def sumOfDivisior(n):
    l = 0
    for i in xrange(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if i != n/i: 
                l+=i
                l+=(n/i)
            else:
                l+=i   # for square numbers
    l = l-n  # don't include the number itself
    return l

def abundant(num):
    if sumOfDivisior(num) > num:
        return True
    else:
        return False

abundants = [x for x in xrange(1, 28124) if abundant(x)]

start = time.time()
dicten={}
length= len(abundants)
for i in xrange(0,length):		
	for j in xrange(i, length):
		sum = abundants[i] + abundants[j]
		if sum not in dicten:
			dicten[sum] = sum			
listen = list(range(1,28123+1))
print "time :" + str(time.time()-start)

sum=0
for item in listen:
	if item not in dicten:
		sum +=item
print sum



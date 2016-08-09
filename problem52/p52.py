def permutation(x,y):
	x = ''.join(sorted(str(x)))
	y = ''.join(sorted(str(y)))
	return x == y

num,consecutives = 0,0
while consecutives < 6:
	num +=1
	consecutives = 1
	for x in xrange(2,7):
		if permutation(num, x*num):
			consecutives+=1
		else:
			break
print num

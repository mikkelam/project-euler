def ispalindrome(num):
	num = str(num)
	return num == num[::-1]

def reverse(num):
	num = str(num)
	return int(num[::-1])

def lychrel(num):
	l = True
	for x in xrange(50):
		num = num + reverse(num)
		if ispalindrome(num):
			l = False
			break
	return l
count = 0
for x in xrange(10000):
	if lychrel(x):
		count+=1
print count
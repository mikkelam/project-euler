import math

num = math.factorial(100)
strnum = str(num)
result=0
for c in strnum:
	result += int(c)

print result
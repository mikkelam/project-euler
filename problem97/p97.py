# import math
# num = 28433
# for x in xrange(7830457):
# 	num = num * 2
# 	if math.log10(num)+1 > 10:
# 		num = num % 10000000000
# print num+1
print ((28433*(2**7830457))+1)%(10**10)
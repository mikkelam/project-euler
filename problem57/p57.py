from fractions import gcd
from time import sleep
def lenm(num):
	return len(str(num))

exp = 2
num,den = 7,5
pnum,pden = 3,2

count = 0

while exp<=1000:
	if lenm(num)>lenm(den):
		count+=1
	num,pnum = num*2+pnum, num
	den,pden = (den*2)+pden, den
	exp+=1


print count
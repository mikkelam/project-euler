from decimal import *
getcontext().prec = 2500


def cycledigits(strng):
	sub1,sub3 = "",""
	cycle=0
	s1=strng[3:10]
	s2= strng[5:17]
	if s1 in s2:
		return 0

	for i in xrange(len(strng)/2):
		sub1 +=strng[i]
		sub2 = ""
		length = len(sub1)
		for j in xrange(i+1,length+i+1):
			sub2+=strng[j]

			#print str(i) + ": " +  sub1 + " " + sub2
			if sub1 == sub2:
				#print "FOUND ONE: " + sub1 + " " + sub2

				if length > cycle:
					if sub3 == sub1[:length/2] and length > 3:
						return cycle
					else:
						cycle= length	
						sub3= sub1

	return cycle

def assignment():
	greatest=0
	number=0

	for i in xrange(2,1000):
		strng= str((Decimal(1.0)/Decimal(i)))
		strng = strng[2:]
		#print strng
		digits = cycledigits(strng)
		if digits > greatest:
				greatest= digits
				number=i
	return greatest,number
print assignment()
#stir = str((Decimal(1.0)/Decimal(109.0)))[2:]
#print stir
#print cycledigits(stir)	

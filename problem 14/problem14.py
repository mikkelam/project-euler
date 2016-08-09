def Collatz(num):	
	count=0
	while num!= 1:
		if num%2==0:
			num=num/2
		else:
			num= (3*num) + 1
		count +=1
	return count

def call_collatz(start):
	greatest=0
	index=0
	while 0<start:
		result = Collatz(start)
		if result > greatest:
			greatest=result
			index=start
		start -= 1
	return greatest,index

print call_collatz(999999)


numbers = range(0, 1000)
multiplicatives = set([
	n for n in numbers 
		if n % 3 == 0
		or n % 5 == 0])
answer = sum(multiplicatives)
print(answer)
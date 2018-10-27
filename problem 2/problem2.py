
fib_table = {1: 1, 2: 2}

def fib(n: int) -> int:
	if n in fib_table:
		return fib_table[n]
	else:
		fib_table[n] = fib(n-1) + fib(n-2)
		return fib_table[n]

i = 1
while True:
	result = fib(i)
	if result > 4000000:
		del fib_table[i]
		break
	i += 1
answer = sum([v for i, v in  fib_table.items() if v % 2 ==0])

print(answer)

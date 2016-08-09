def fib(n, memo={0:0, 1:1}):
    if n not in memo:
        memo[n] = fib(n-1) + fib(n-2)
    return memo[n]
   
def assignment():
 	x=1
	while len(str(fib(x)))!= 1000:
		x+=1

	return x 


print assignment()
from time import sleep
def ispalindrome(num):
	return num == num[::-1]

def main():
	palindromes = []
	for x in xrange(1,1000000):
		base10 = [i for i in str(x)]
		base2 = [i for i in str(bin(x)[2:])]
		if ispalindrome(base2) and ispalindrome(base10):
			palindromes.append(x)
	return sum(palindromes)

print main()
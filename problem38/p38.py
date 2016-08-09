def pandigital9(nums):
	if len(nums) != 9:
		return False
	lst = [x for x in xrange(1,9)]
	for num in lst:
		if num not in nums:
			return False
	return True
def main():
	candids = []
	for x in xrange(2,9999):
		lst = []
		count = 1
		while len(lst) < 9:
			lst.extend([int(a) for a in str(x*count)])
			count += 1
		if pandigital9(lst):
			candids.append(int(''.join(map(str,lst))))
	return max(candids)
print main()
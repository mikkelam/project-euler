from itertools import permutations
def pandigital(nums):
	lst = [x for x in xrange(1,len(nums)+1)]
	for num in lst:
		if num not in nums:
			return False
	return True
def main():
	candids = []
	perms = permutations([1,2,3,4,5,6,7,8,9],5)
	for perm in perms:
		prod = int(''.join(map(str,perm[0:3]))) * int(''.join(map(str,perm[3:])))
		prodlst = [int(x) for x in str(prod)]
		prodlst.extend(perm)
		if len(prodlst) < 10:
			if pandigital(prodlst):
				if prod not in candids:
					candids.append(prod)
		prod = int(perm[0]) * int(''.join(map(str,perm[1:])))
		prodlst = [int(x) for x in str(prod)]
		prodlst.extend(perm)
		if len(prodlst) < 10:
			if pandigital(prodlst):
				if prod not in candids:
					candids.append(prod)
	return candids, sum(candids)
print main()
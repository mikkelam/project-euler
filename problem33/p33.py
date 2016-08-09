from itertools import permutations
from operator import mul

def main():
	candids = []
	for x in xrange(1010,9999):
		lst = [int(a) for a in str(x)]
		val1 = int(''.join(map(str,lst[0:2])))
		val2 = int(''.join(map(str,lst[2:])))
		if len(str(val2))==1 or val1 == val2:
			continue
		div = float(val1)/val2
		x,y = False,False
		if lst[0] == lst[2]:
			x,y = 1,3
		elif lst[0] == lst[3]:
			x,y = 1,2
		elif lst[1] == lst[2]:
			x,y = 0,3
		elif lst[1] == lst[3]:
			x,y = 0,2
		if x and y:
			if lst[x] != 0 and lst[y] != 0:
				if (float(lst[x]) / lst[y]) == div:
					candids.append(div)
	return reduce(mul, candids)
print main()
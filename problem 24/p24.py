import itertools
generator = itertools.permutations([0,1,2,3,4,5,6,7,8,9])
lst = list(generator)
strgs = []



#tuple to string
for tupl in lst:
	#strgs.append(((((str(tupl).replace("(", "")).replace(")","")).replace(",", "")).replace(" ", "")))
	strgs.append(''.join(map(str,tupl)))

strgs.sort()
print strgs[999999]

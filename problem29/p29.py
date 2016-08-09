def main():
	s = []
	for a in xrange(2,101):
		for b in xrange(2,101):
			x = a**b
			if x not in s:
				s.append(x)		

	return len(s)
print(main())




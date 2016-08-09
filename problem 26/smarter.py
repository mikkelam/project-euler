import time

def cycle_length(d):
	rs = set()
	r = 1%d
	while not (r == 0 or r in rs):
		print r
		rs.add(r)
		r = r*10%d
		#time.sleep(1)
	return 0 if r == 0 else len(rs)

# start = time.time()
#print max(xrange(1,1000), key=cycle_length)
# end = time.time() - start

print cycle_length(7)
# print 'It took %f seconds' % end

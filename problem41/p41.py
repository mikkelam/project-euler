from pyprimes import primes

def pandigital(x):
    nums = [int(x) for x in str(x)]
    lst = range(1,len(nums)+1)
    for l in lst:
        if l not in nums:
            return False
    return True




p = primes()
best = 1
for x in xrange(1000000):
    prm = next(p)
    if pandigital(prm):
        best = prm
print best

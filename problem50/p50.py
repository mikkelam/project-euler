from pyprimes import primes_below, isprime
from copy import deepcopy
primes = list(primes_below(1000000))

best = 2
nums = []
bestnums= []
x = 0
lenprimes = len(primes)-1
for x in xrange(0,lenprimes):
    num = 0
    nums = []
    y = x
    while num < 1000000:
        num += primes[y]
        nums.append(primes[y])
        if isprime(num) and num < 1000000 and num > best and len(nums) > len(bestnums):
            best = num 
            bestnums = deepcopy(nums)
        y+=1
        if y > lenprimes:
            break
print best
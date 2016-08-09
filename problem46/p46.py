from pyprimes import isprime, primes_below
num = 2
while True:
    if not isprime(num) and num % 2 == 1:
        for prime in primes_below(num):
            sqnum = 1
            while num > (prime + 2*(sqnum**2)):
                sqnum+=1
            if num == (prime + 2*(sqnum**2)):
                break

        if num != (prime + 2*(sqnum**2)):
            break
    num += 1
print num
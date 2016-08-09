from pyprimes import primes_below,isprime

def isperm(v,w):
    w = [x for x in str(w)]
    for l in str(v):
        if l not in w:
            return False
        else:
            w.remove(l)

    return True

p = list(primes_below(10000))
primes = [x for x in p if x>999]
sols = []
for x in xrange(len(primes)):
    p1 = primes[x]
    for y in xrange(x+1, len(primes)):
        p2 = primes[y]
        increaser = p2-p1
        if isperm(p1,p2):
            for z in xrange(y+1, len(primes)):
                p3 = primes[z]
                if p2+increaser==p3:
                    if  isperm(p2,p3):
                        sols.append([p1,p2,p3])


for a,b,c in sols:
    print a,b,c,''.join(map(str,[a,b,c]))

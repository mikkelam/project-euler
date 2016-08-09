import math
def main():
    candids = []
    for p in xrange(1,1001):
        sols = 0
        for a in xrange(1, p/2):
            for b in xrange(a, p/2):
                c = math.sqrt(a**2 + b**2)
                if (a+b+c)==p:
                    sols += 1
        candids.append((sols,p))
    return sorted(candids, key=lambda x: x[0], reverse=True)[0]
print main()
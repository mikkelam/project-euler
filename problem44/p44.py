import math
def pentagonal(n):
    return (n*(3*n-1))/2

def is_pentagonal(n):
    return (1+(24*n+1)**0.5)/6 % 1 == 0

def main():
    i, k = 1,1
    pj = pentagonal(i)
    while True:
        pk = pentagonal(k+1)
        if (pj + pk) < pentagonal(k+2):
            i += 1
            k = i
            pj = pentagonal(i)
        elif is_pentagonal(pj + pk):
            if is_pentagonal(pk-pj):
                return abs(pk-pj)
        k+=1
print main()
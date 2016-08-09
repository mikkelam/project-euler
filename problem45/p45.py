from math import sqrt
def is_tri(n):
    return (1/2.0*(-sqrt(8*n+1)-1))%1==0
def is_pen(n):
    return 1/6.0*(sqrt(24*n+1)+1)%1==0
def is_hex(n):
    return (-1/4.0*(1-sqrt(8*n+1)) + 1/2.0)%1==0
def tri(n):
    return n*(n+1)/2
# def pen(n):
#     return n*(3*n-1)/2
# def hex(n):
#     return n*(2*n-1)
def main():
    n = 286
    while True:
        t = tri(n)
        if is_pen(t):
            if is_hex(t):
                return t
        n+=1    
print main()
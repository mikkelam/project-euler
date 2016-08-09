def t(n):
    return (n*(n+1))/2

def lord(l):
    return ord(l)-64

def lordword(word):
    return sum([lord(l) for l in word])

def main():
    triangles = [t(x) for x in xrange(10000)]

    with open('words.txt', 'r') as f:
        words = f.read()
    words = words.replace('"', '').split(',')

    amount = 0
    for word in words:
        if lordword(word) in triangles:
            amount += 1
    return amount
print main()
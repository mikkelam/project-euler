s = ''.join([str(i) for i in xrange(1, 1000000)])
print int(s[0]) * int(s[10-1]) * int(s[100-1]) * int(s[1000-1]) * int(s[10000-1]) * int(s[100000-1])  * int(s[1000000-1])
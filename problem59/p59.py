from time import sleep
with open("cipher.txt") as f:
	message = f.read().split(",")
message = map(int, message)

winner = ""
ords = range(ord("a"), ord("z")+1)
for k1 in ords:
	for k2 in ords:
		for k3 in ords:
			decoded = []
			key = [k1,k2,k3]
			i = 0
			for m in message:
				decoded.append(m ^ key[i])
				i = (i+1)%3


			candidate = ''.join(map(chr, decoded))
			if candidate.find("Gospel")!= -1:
				winner = candidate

print sum([ord(x) for x in winner])
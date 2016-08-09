def main():
	coinset = 0
	coins = 'lol'
	p1,p2,p5,p10,p20,p50,p100,p200=0,0,0,0,0,0,0,0	
	for p1 in xrange(0,201,1):
		if p1+p2+p5+p10+p20+p50+p100+p200> 200:
			break
		for p2 in xrange(0,201,2):
			if p1+p2+p5+p10+p20+p50+p100+p200> 200:
				break
			for p5 in xrange(0,201,5):
				if p1+p2+p5+p10+p20+p50+p100+p200> 200:
					break
				for p10 in xrange(0,201,10):
					if p1+p2+p5+p10+p20+p50+p100+p200> 200:
						break
					for p20 in xrange(0,201,20):
						if p1+p2+p5+p10+p20+p50+p100+p200> 200:
							break
						for p50 in xrange(0,201,50):
							if p1+p2+p5+p10+p20+p50+p100+p200> 200:
								break
							for p100 in xrange(0,201,100):
								if p1+p2+p5+p10+p20+p50+p100+p200> 200:
									break
								for p200 in xrange(0,201,200):
									if p1+p2+p5+p10+p20+p50+p100+p200== 200:
										# coins = (p1,p2,p5,p10,p20,p50,p100,p200)
										# if coins not in coinset:
										# sleep(0.01)	
										# print (p1,p2,p5,p10,p20,p50,p100,p200)
										coinset+=1
								p200=0
							p100=0
						p50=0
					p20=0
				p10=0
			p5=0
		p2=0

		# print '&'

	return coinset

print main()
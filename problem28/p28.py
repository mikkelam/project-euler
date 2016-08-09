



counter=2
round=2

diagonals =[1]

rounddiagonals=[]
while round<=1001:
	if counter % round == 1:
		diagonals.append(counter)
		rounddiagonals.append(counter)
		

	if len(rounddiagonals)==4:

		rounddiagonals=[]
		round +=2

	counter+=1

print sum(diagonals)
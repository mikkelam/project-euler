
def load_tri():
	f = open('tri', 'r')
	arrstr = f.readlines()
	arr=[]
	for ele in arrstr:
		arr.append(ele.replace("\n", ""))

	triangle= []

	for s in arr:
		triangle.append(map(int, s.split(' ')))

	return triangle[::-1]


triangle = load_tri()


def maxpath(row, index):
	current= triangle[row][index]
	left = index
	right = index+1
	next = row-1
	if row==1:
		return current + max(triangle[next][left], triangle[next][right])
	else:
		return current + max(maxpath(next, left), maxpath(next,right))

print maxpath(14,0)
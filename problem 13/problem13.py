f = open('/home/mikkel/Dropbox/Programmering/project_euler/problem 13/text', 'r')

arrstr = f.readlines()

arr=[]
for ele in arrstr:
	arr.append(int(ele.replace("\n", "")))

sum=0
for ele in arr:
	sum+= ele
print sum
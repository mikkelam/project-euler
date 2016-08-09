

def a_pos(char):
	return ord(char)-96

def a_val(name):
	score=0
	for char in name:
		score+=a_pos(char)
	return score

def a_score(name, pos):
	return pos * a_val(name.lower())


def assignment(names):
	scores = []
	x=1
	for name in names:
		scores.append(a_score(name, x))
		x+=1
	return sum(scores)


f = open('/home/mikkel/Dropbox/Programmering/project_euler/problem 22/names.txt', 'r')
filetxt = f.readline()
replaced = filetxt.replace('"', "")
names = replaced.split(',')
names.sort()

print assignment(names)
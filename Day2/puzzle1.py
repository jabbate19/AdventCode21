import subprocess
def copy(data):
	subprocess.run('pbcopy',universal_newlines=True,input=str(data))

with open('input.txt') as file:
	horiz=0
	depth=0
	aim=0
	for line in file:
		l = line.split()
		if l[0] == 'forward':
			horiz += int(l[1])
			depth += aim*int(l[1])
		elif l[0] == 'down':
			aim += int(l[1])
		else:
			aim -= int(l[1])
	print(horiz*depth)
	copy(horiz*depth)


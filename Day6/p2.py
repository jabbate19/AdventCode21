import subprocess
def copy(data):
	subprocess.run('pbcopy',universal_newlines=True,input=str(data))

with open('input.txt') as file:
    lines = [line for line in file]

nums = list(map(int,lines[0].split(',')))

counts = [0 for _ in range(9)]
for n in nums:
    counts[n] += 1

to_be_added = []
names = ['SUN','MON','TUE','WED','THUR','FRI','SAT']
for day in range(256):
    print(counts)
    next_day = counts.pop(0)
    counts[6] += next_day
    counts.append(next_day)

copy(sum(counts))


import subprocess
def copy(data):
	subprocess.run('pbcopy',universal_newlines=True,input=str(data))

with open('input.txt') as file:
    lines = [line for line in file]

graph = []
for line in lines:
    line = line.strip('\n')
    graph.append(list(map(int,(c for c in line))))

rows = len(graph)
cols = len(graph[0])

for a in graph:
    print(a)

s=0
for r in range(rows):
    for c in range(cols):
        val = graph[r][c]
        left = c-1
        right = c+1
        top = r - 1
        bottom = r + 1
        valid = []
        if left >= 0:
            valid.append(graph[r][left])
        if right < cols:
            valid.append(graph[r][right])
        if top >= 0:
            valid.append(graph[top][c])
        if bottom < rows:
            valid.append(graph[bottom][c])
        good = True
        for v in valid:
            if v <= val:
                good = False
                break
        if good:
            s += val + 1

copy(s)
        
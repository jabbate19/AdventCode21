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

lows = []
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
            lows.append((r,c))

used=[]
def steps(r,c):
    val = graph[r][c]
    if not val in used:
        used.append((r,c))
    used.append((r,c))
    print('val:',val)
    left = c-1
    right = c+1
    top = r - 1
    bottom = r + 1
    out = 1
    if left >= 0:
        if val - graph[r][left] <= -1 and not (r,left) in used and graph[r][left] != 9:
            print('val:',val,'left',graph[r][left])
            used.append((r,left))
            out += steps(r,left)
    if right < cols:
        if val - graph[r][right] <= -1 and not (r,right) in used and graph[r][right] != 9:
            print('val:',val,'right',graph[r][right])
            used.append((r,right))
            out += steps(r,right)
    if top >= 0:
        if val - graph[top][c] <= -1 and not (top,c) in used and graph[top][c] != 9:
            print('val:',val,'top',graph[top][c])
            used.append((top,c))
            out += steps(top,c)
    if bottom < rows:
        if val - graph[bottom][c] <= -1 and not (bottom,c) in used and graph[bottom][c] != 9:
            print('val:',val,'bottom',graph[bottom][c])
            used.append((bottom,c))
            out += steps(bottom,c)
    return out

scores = []
for low in lows:
    a = steps(low[0],low[1])
    scores.append(a)

scores = sorted(scores,reverse=True)[0:3]
s=1
for score in scores:
    print(score)
    s*=score

copy(s)
        
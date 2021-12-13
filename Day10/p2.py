import subprocess
def copy(data):
	subprocess.run('pbcopy',universal_newlines=True,input=str(data))

with open('test.txt') as file:
    lines = [line for line in file]

opening = set('([{<')
closing = set(')]}>')
opp = {
    '(' : ')',
    '[' : ']',
    '{' : '}',
    '<' : '>'
}
pts = {
    ')' : 1,
    ']' : 2,
    '}' : 3,
    '>' : 4
}

scores = []
req = []
for line in lines:
    req = []
    line = line.strip('\n')
    for i in range(len(line)):
        c = line[i]
        if c in opening:
            req.append(opp[c])
        else:
            print(req)
            expected = req.pop()
            print("Popped",expected)
            if c != expected:
                break
    else:
        if req:
            score = 0
            print(line)
            print(req)
            for _ in range(len(req)):
                r = req.pop()
                print(r)
                score *= 5
                score += pts[r]
            print(score)
            print()
            scores.append(score)

scores.sort()
print(scores)
print(scores[len(scores)//2])
copy(scores[len(scores)//2])
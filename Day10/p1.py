import subprocess
def copy(data):
	subprocess.run('pbcopy',universal_newlines=True,input=str(data))

with open('input.txt') as file:
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
    ')' : 3,
    ']' : 57,
    '}' : 1197,
    '>' : 25137
}

score = 0
req = []
for line in lines:
    line = line.strip('\n')
    for i in range(len(line)):
        c = line[i]
        if c in opening:
            req.append(opp[c])
        else:
            expected = req.pop()
            if c != expected:
                print(line,i,c,expected)
                score += pts[c]
                break

copy(score)
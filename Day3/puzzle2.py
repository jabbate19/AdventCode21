import subprocess
def copy(data):
	subprocess.run('pbcopy',universal_newlines=True,input=str(data))

with open('input.txt') as file:
    lines = []
    o2 = 0
    co2 = 0
    for line in file:
        lines.append(line)
    for j in range(2):
        l = lines[:]
        print(len(l))
        for i in range(12):
            if len(l) == 1:
                if not j:
                    o2 = int(l[0],2)
                else:
                    co2 = int(l[0],2)
                break
            ones = 0
            zeroes = 0
            for line in l:
                if line[i] == '1':
                    ones += 1
                else:
                    zeroes += 1
            if ones >= zeroes:
                target = '1'
            else:
                target = '0'
            if not j:
                l = list(filter(lambda x: x[i] == target, l))
                print(len(l))
                o2 = int(l[0],2)
            else:
                l = list(filter(lambda x: x[i] != target, l))
                print(len(l))
                co2 = int(l[0],2)
    copy(co2*o2)



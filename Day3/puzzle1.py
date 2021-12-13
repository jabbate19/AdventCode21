import subprocess
def copy(data):
	subprocess.run('pbcopy',universal_newlines=True,input=str(data))

with open('input.txt') as file:
    lines = []
    for line in file:
        lines.append(line)
    gamma = ''
    epsilon = ''
    for i in range(12):
        print(i)
        ones = 0
        zeroes = 0
        for line in lines:
            if line[i] == '1':
                ones += 1
            else:
                zeroes += 1
        print(ones,zeroes)
        if ones > zeroes:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'
    print(gamma,epsilon)
    gamma = int(gamma,2)
    epsilon = int(epsilon,2)
    print(gamma*epsilon)



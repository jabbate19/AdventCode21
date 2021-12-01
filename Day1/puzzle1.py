with open('input.txt') as file:
    vals = []
    for line in file:
        vals.append(int(line))
    larger = 0
    for i in range(1,len(vals)):
        if vals[i] > vals[i-1]:
            larger += 1
print(larger)


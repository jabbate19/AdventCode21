import subprocess
def copy(data):
	subprocess.run('pbcopy',universal_newlines=True,input=str(data))

with open('input.txt') as file:
    lines = [line.strip('\n') for line in file]

field = [[0 for _ in range(1000)] for _ in range(1000)]

points = []
for line in lines:
    sub = line.split(' -> ')
    out = []
    for i in range(2):
        nums = [int(x) for x in sub[i].split(',')]
        out.append(tuple(nums))
    points.append(tuple(out))

for s in points:
    x1 = s[0][0]
    y1 = s[0][1]
    x2 = s[1][0]
    y2 = s[1][1]
    if x1 == x2:
        c=0
        if y1 < y2:
            for y in range(y1,y2+1):
                c+=1
                field[y][x1] += 1
        elif y1 > y2:
            for y in range(y2,y1+1):
                c+=1
                field[y][x1] += 1
        else:
            field[y1][x1] += 1
        print(x1,y1,x2,y2,c)
    elif y1 == y2:
        c=0
        if x1 < x2:
            for x in range(x1,x2+1):
                c+=1
                field[y1][x] += 1
        elif x1 > x2:
            for x in range(x2,x1+1):
                c+=1
                field[y1][x] += 1
        else:
            field[y1][x1] += 1
        print(x1,y1,x2,y2,c)
    else:
        c=0
        if x1 < x2:
            left = (x1,y1)
            right = (x2,y2)
        else:
            right = (x1,y1)
            left = (x2,y2)
        d = 0
        if right[1] > left[1]:
            d = 1
        else:
            d = -1
        x = x1
        y = y1
        if d == 1:
            while x <= right[0] and y <= right[1]:
                print(x,y)
                field[x1][y1] += 1
                x += 1
                y += 1
                c += 1
        else:
            while x <= right[0] and y >= right[1]:
                print(x,y)
                field[x1][y1] += 1
                x += 1
                y += -1
                c += 1
        print(x1,y1,x2,y2,c,d, left, right)

count = 0
for row in field:
    #print(row)
    for val in row:
        if val >= 2:
            count += 1

copy(count)

with open('input.txt') as file:
    vals = list(map(int(file)))
    sums = [sum(vals[i:i+3]) for i in range(len(vals)-2)]
    larger = sum(1 for i in range(1,len(sums)) if sums[i] > sums[i-1])
print(larger)


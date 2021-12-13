import subprocess
import time
def copy(data):
	subprocess.run('pbcopy',universal_newlines=True,input=str(data))

start = time.perf_counter()

with open('input.txt') as file:
    lines = [line for line in file]

data = list(map(int,lines[0].split(',')))

min_fuel = -1
min_target = -1
for target in range(min(data),max(data)+1):
    fuel = 0
    for sub in data:
        fuel += sum(range(1,abs(target-sub)+1))
    if min_fuel == -1 or fuel < min_fuel:
        min_fuel = fuel
        min_target = target

copy(min_fuel)

print(time.perf_counter()-start)
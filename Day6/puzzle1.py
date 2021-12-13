import subprocess
def copy(data):
	subprocess.run('pbcopy',universal_newlines=True,input=str(data))

with open('input.txt') as file:
    lines = [line for line in file]

nums = list(map(int,lines[0].split(',')))
for c in range(256):
    print(c)
    #print(nums)
    for i in range(len(nums)):
        nums[i] -= 1
        if nums[i] == -1:
            nums[i] = 6
            nums.append(8)

copy(len(nums))
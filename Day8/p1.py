import subprocess
def copy(data):
	subprocess.run('pbcopy',universal_newlines=True,input=str(data))

with open('input.txt') as file:
    lines = [line.split(' | ')[1] for line in file]

NUM_DICT = {
    'abcefg' : 0,
    'cf' : 1,
    'acdeg' : 2,
    'acdfg' : 3,
    'bcdf' : 4,
    'abdfg' : 5,
    'abdefg' : 6,
    'acf' : 7,
    'abcdefg' : 8,
    'abcdfg' : 9
}
def get_number(num_str):
    for key in NUM_DICT:
        if len(num_str) == len(key):
            good = True
            for c in key:
                if not c in num_str:
                    good = False
                    break
            if good:
                return NUM_DICT[key]
    return None

count = 0
for line in lines:
    for num_str in line.split():
        if len(num_str) in [2,3,7,4]:
            count += 1
        """
        num = get_number(num_str)
        print(num_str,num)
        if num in [1,4,7,8]:
            count += 1
        """

copy(count)
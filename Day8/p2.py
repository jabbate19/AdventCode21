import subprocess
def copy(data):
	subprocess.run('pbcopy',universal_newlines=True,input=str(data))

with open('input.txt') as file:
    lines = [line.split(' | ') for line in file]

def get_number(num_str,num_dict):
    for key in num_dict:
        if len(num_str) == len(key):
            good = True
            for c in key:
                if not c in num_str:
                    good = False
                    break
            if good:
                return num_dict[key]
    return None

def convert(s):
    new = ""
    for x in s:
        new += x
    return new

total = 0
for line in lines:
    zero = None
    one = None
    two = None
    three = None
    four = None
    five = None
    six = None
    seven = None
    eight = None
    nine = None
    tests = line[0].split()
    for num_str in tests:
        if len(num_str) == 2:
            one = set(num_str)
        elif len(num_str) == 3:
            seven = set(num_str)
        elif len(num_str) == 4:
            four = set(num_str)
        elif len(num_str) == 7:
            eight = set(num_str)
    print("1478",one,four,seven,eight)
    for num_str in tests:
        if len(num_str) == 6:
            if len(one - set(num_str)):
                six = set(num_str)
            else:
                if len(four - set(num_str)):
                    zero = set(num_str)
                else:
                    nine = set(num_str)
    print("069",zero, six, nine)
    for num_str in tests:
        if len(num_str) == 5:
            if len(four-set(num_str)) == 2:
                two = set(num_str)
            else:
                if len(one-set(num_str)):
                    five = set(num_str)
                else:
                    three = set(num_str)
    print("235",two,three,five)
    num_dict = {
        convert(zero) : 0,
        convert(one) : 1,
        convert(two) : 2,
        convert(three) : 3,
        convert(four) : 4,
        convert(five) : 5,
        convert(six) : 6,
        convert(seven) : 7,
        convert(eight) : 8,
        convert(nine) : 9
    }
    pin = line[1].split()
    val = 0
    for i in range(len(pin)):
        num_str = pin[i]
        val += get_number(num_str, num_dict) * (10 ** (3-i))
    total += val
copy(total)





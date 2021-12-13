import subprocess
def copy(data):
	subprocess.run('pbcopy',universal_newlines=True,input=str(data))

with open('input.txt') as file:
    lines = [line for line in file]
pulls = [int(x) for x in lines[0].split(',')]

def get_cards():
    cards = []
    card = []
    for i in range(2,len(lines)):
        if i%6 == 1 and card:
            print("NEW\n",card)
            cards.append(card)
            card = []
        else:
            card.append(list(map(int,lines[i].split())))
    return cards

def check_cards(cards, called, verbose = False):
    for card in cards:
        for row in card:
            good = True
            for val in row:
                if not val in called:
                    good = False
                    break
            if verbose:
                print(row,called,good)
            if good:
                used = row
                break
        if good:
            s = 0
            for row in card:
                for val in row:
                    if not val in called:
                        s += val
            if verbose:
                print("USED:",used)
                print("VAL:", s, called[-1],s * called[-1])
            return s * called[-1]
        for i in range(5):
            good = True
            for row in card:
                if not row[i] in called:
                    good = False
                    break
            if verbose:
                print([row[i] for row in card],called,good)
            if good:
                used = [row[i] for row in card]
                break
        if good:
            if verbose:
                print("USED:",used)
            s = 0
            for row in card:
                for val in row:
                    if val in used:
                        break
                    else:
                        s += val
            return s * called[-1]
    return 0

def main():
    #for card in get_cards():
    #    for line in card:
    #        print(line)
    #    print()
    cards = get_cards()
    called = []
    for pull in pulls:
        called.append(pull)
        #check = check_cards(cards,called, called == [7,4,9,5,11,17,23,2,0,14,21,24])
        check = check_cards(cards,called)
        if check:
            copy(check)
            break

if __name__ == '__main__':
    main()



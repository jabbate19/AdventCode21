import subprocess
def copy(data):
	subprocess.run('pbcopy',universal_newlines=True,input=str(data))

with open('input.txt') as file:
    lines = [line for line in file]
pulls = [int(x) for x in lines[0].split(',')]

cards = []

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

def check_cards(called, verbose = False):
    print(len(cards))
    rec = called[-1]
    out = []
    for card in cards:
        for row in card:
            good = True
            if rec in row:
                for val in row:
                    if not val in called:
                        good = False
                        break
                if verbose:
                    print(row,called,good)
            else:
                good = False
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
            out.append((card, s * called[-1]))
        for i in range(5):
            col = [row[i] for row in card]
            good = True
            if rec in col:
                for val in col:
                    if not val in called:
                        good = False
                        break
                if verbose:
                    print(col,called,good)
            else:
                good = False
            if good:
                used = col
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
            out.append((card, s * called[-1]))
    return out

def main():
    global cards
    #for card in get_cards():
    #    for line in card:
    #        print(line)
    #    print()
    cards = get_cards()
    called = []
    win = []
    for pull in pulls:
        called.append(pull)
        #check = check_cards(cards,called, len(called) > len([7,4,9,5,11,17,23,2,0,14,21,24,10,16,13]))
        check = check_cards(called,False)
        for w in check:
            print(w[1])
            try:
                cards.remove(w[0])
            except ValueError:
                pass
            win.append(w)
    print(win[-1][1])
    for row in win[-1][0]:
        print(row)


if __name__ == '__main__':
    main()



list_ch = ['V', 'H', 'T', 'A', 'G', 'E', 'O', 'L', 'R']
n = 2

def theLoop( list, i, n, message):
    for l in list:
        if i < n:
            theLoop(list, i+1, n, message+l)
        elif i == n:
            print message+l

theLoop( list_ch, 1, n, '')

print list_ch
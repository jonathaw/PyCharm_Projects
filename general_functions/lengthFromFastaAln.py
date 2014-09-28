import sys
IN = open(sys.argv[1], 'r')
NAME = sys.argv[2].upper()
seq = ''
for line in IN:
    if line[1:5] == NAME:
        for i_line in IN:
            if i_line[0] != '>':
                seq += i_line.rstrip()
            else:
                break
cleaned = seq.translate(None, '-')
print len(cleaned)
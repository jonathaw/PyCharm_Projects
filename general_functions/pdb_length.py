import sys
seq = ''
for line in open(sys.argv[1], 'r'):
    if line[0] == '>' or line[0] == '\n':
        continue
    seq += line.strip()

print len(seq)
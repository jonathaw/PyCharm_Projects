import re, sys

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

#print seq

if NAME == '1OHZ':
    pat = re.compile("V-*F-*L-*F-*A.*")
elif NAME == '2B59':
    pat = re.compile("N-*F-*A-*L-*A.*")
elif NAME == '2CCL':
    pat = re.compile("V-*F-*L-*F-*A.*")
elif NAME == '2OZN':
    pat = re.compile("R-*V-*L-*V-*S.*")
elif NAME == '2VN5':
    pat = re.compile("S-*F-*L-*F-*L.*")
elif NAME == '2Y3N':
    pat = re.compile("N-*F-*G-*R-*L.*")
elif NAME == '3UL4':
    pat = re.compile("A-*V-*L-*Y-*L.*")
elif NAME == '3KCP':
    pat = re.compile("N-*F-*A-*L-*A.*")
elif NAME == '4DH2':
    pat = re.compile("V-*F-*L-*F-*D.*")
elif NAME == '4IU2':
    pat = re.compile("F-*V-*A-*S-*G.*")
elif NAME == '4UYP':
    pat = re.compile("S-*M-*T-*F-*E.*")
elif NAME == '4UYQ':
    pat = re.compile("S-*M-*T-*F-*E.*")

#print pat.search(seq).start(), seq[pat.search(seq).start()]
subseq = seq[0:pat.search(seq).start() + 1]
cleaned = subseq.translate(None, '-')
print len(cleaned)
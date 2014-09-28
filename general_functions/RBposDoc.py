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
    pat = re.compile("S-*T-*D-*L-*T.*")
elif NAME == '2B59':
    pat = re.compile("L-*L-*D-*V-*A.*")
elif NAME == '2CCL':
    pat = re.compile("S-*T-*D-*L-*T.*")
elif NAME == '2OZN':
    pat = re.compile("I-*G-*D-*L-*A.*")
elif NAME == '2VN5':
    pat = re.compile("A-*L-*D-*F-*A.*")
elif NAME == '2Y3N':
    pat = re.compile("M-*A-*D-*V-*M.*")
elif NAME == '3UL4':
    pat = re.compile("D-*E-*D-*Y-*I.*")
elif NAME == '3KCP':
    pat = re.compile("L-*L-*D-*V-*A.*")
elif NAME == '4DH2':
    pat = re.compile("I-*S-*D-*Y-*V.*")
elif NAME == '4IU2':
    pat = re.compile("G-*R-*D-*A-*T.*")
elif NAME == '4UYP':
    pat = re.compile("S-*I-*D-*A-*V.*")
elif NAME == '4UYQ':
    pat = re.compile("I-*N-*D-*A-*V.*")

#print pat.search(seq).start(), seq[pat.search(seq).start()]
subseq = seq[0:pat.search(seq).start()+1]
cleaned = subseq.translate(None, '-')
print len(cleaned)
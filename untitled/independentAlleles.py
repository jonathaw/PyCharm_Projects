k = 2
n = 1

AA = [0.5]
Aa = [0.1]
aa = [0.5]

i = 1
while i <= k:
    new_AA = 1*AA[i-1] + 0.5*Aa[i-1] + 0*aa[i-1]
    new_Aa = 1*AA[i-1] + 1*Aa[i-1] + 1*aa[i-1]
    new_aa = 0*AA[i-1] + 0.5*Aa[i-1] + 1*aa[i-1]
    AA.append(new_AA)
    Aa.append(new_Aa)
    aa.append(new_aa)

    i += 1

print AA, Aa, aa
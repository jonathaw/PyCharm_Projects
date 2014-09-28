n = 5
perm = [5, 1, 4, 2, 3]

# increase =[]
# decrease =[]
# print len(perm)
# for i, ele in enumerate(perm):
#     inc = [ele]
#     dec = [ele]
#     now = i + 1
#     print i, now, inc, dec
#     while now <= len(perm):
#         print perm[now], inc[len(inc)-1]
#         if perm[now] > inc[len(inc)-1]:
#             inc.append(perm[now])
#         if perm[now] < dec[len(dec)-1]:
#             dec.append(perm[now])
#         now += 1
#     increase.append(inc)
#     decrease.append(dec)
#
# print increase
# print decrease


increase = []
decrease = []

j = 0
while j <= len(perm)-1:
    inc = [perm[j]]
    dec = [perm[j]]

    now = j + 1
    while j <= len(perm)-1:
        if perm[j] < dec[len(dec)-1]:
            dec.append(perm[j])
        if perm[j] > inc[len(inc)-1]:
            inc.append(perm[j])

        print inc, dec,j, perm[j], dec[len(dec)-1], inc[len(inc)-1]
        j += 1


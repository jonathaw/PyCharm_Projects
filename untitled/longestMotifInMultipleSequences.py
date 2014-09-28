IN = open("/Users/jonathan/Desktop/temp.txt", "r")

dict = {}

for line in IN:
    if line[0] == '>':
        name = line.strip()
        dict[name] = ''
    else:
        dict[name] += line.strip()

shortest = min(dict.values(), key=len)

list = []
i = len(shortest)
while i >= 1:
    j = 0
    while j + i <= len(shortest):
        seg = shortest[j:(j+i)]

        bool = True
        for key in dict:
            if not seg in dict[key]:
                bool = False
                break
        if bool: list.append(seg)
        j += 1
    i -= 1
    if bool: break
print list
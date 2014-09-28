n = 5
seq = [5, 1, 4, 2, 3]
#n = 10
#seq = [7, 3, 9, 4, 6, 10, 8, 2, 1, 5]


def next_num(seq, num, index):
    for j in range(index+1, len(seq)):
        if seq[j] > num:
            return seq[j]


def there_isnt(seq, last, num1, num2):
    print "is_there", last, num1, num2
    for j in range(seq.index(num1)+1, seq.index(num2)-1):
        if seq[j] > last and seq[j] < num2:
            return False
    return True


def bigger_to_end(seq, last, index):
    for j in range(index+1, len(seq)-1):
        print "bigger", last, seq[index], j
        if seq[j] > last:
            print seq[j], "is bigger than ", last
            return True
        else:
            print seq[j], "isn't bigger than" ,last
    False


def iterator(seq, incList):
    for i in seq:
        lis = [i]
        while next_num(seq, lis[-1], seq.index(lis[-1])) is not None:
            num1 = next_num(seq, i, seq.index(lis[-1]))
            num2 = next_num(seq, num1, seq.index(num1))
            print "beginning of loop: li is", lis, "i is ", i, "num1 is ", num1, "num2 is ", num2
            if num2 is None and bigger_to_end(seq, lis[-1], seq.index(num1)):
                num1 = next_num(seq, lis[-1], seq.index(num1))
                num2 = next_num(seq, num1, seq.index(num1))
            elif num2 is None and not bigger_to_end(seq, lis[-1], seq.index(num1)):
                incList.append(lis.append(num1))

            if there_isnt(seq, lis[-1], num1, num2):
                lis.append(num1)
                print "there isn't is True, appending to lis", lis
            else:
                lis.append(next_num(seq, lis[-1], seq.index(num1)))







#### MAIN ####

incList = []
iterator(seq, incList)
print "inList is finally: ", incList
#reverse sequecen
#iterator(reverse sequecne)
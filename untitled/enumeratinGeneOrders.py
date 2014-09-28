import math
n = 6

numbers = [1]

i = 2
while i <= n:
    numbers.append(i)
    i += 1


tot = math.factorial(n)
print tot




for i in numbers:
    list1 = list( numbers )
    list1.remove(i)
    for j in list1:
        list2 = list( list1 )
        list2.remove(j)

        for k in list2:
            list3 = list( list2 )
            list3.remove(k)

            for q in list3:
                list4 = list( list3 )
                list4.remove(q)

                for w in list4:
                    list5 = list(list4)
                    list5.remove(w)
                    for e in list5:
                        print i,j,k,q,w,e
#sum
def sum(*n) :
    i = 0
    for x in n :
        i = i + x
    return i

#avarage
def avarage(*n):
    i = 0
    j = 0
    for x in n :
        i = i + x
        j += 1
    avarage = i / j
    return avarage

#maks
def max (*n):
    max = n[0]
    for i in (n) :
        if (i > max):
            max = i
    return max

#min
def min(*n):
    min = n[0]
    for i in (n) :
        if (i < min):
            min = i
    return min

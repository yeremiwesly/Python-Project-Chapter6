def faktorial (n) :
    faktor = 1
    while (n > 0):
        faktor = faktor * n
        n -= 1
    return faktor

def kombinasi (a, b) :
    c = a - b
    hasil = faktorial (a) / (faktorial (b) * faktorial (c))
    print (hasil)

def permutasi (a, b) :
    c = a - b
    hasil = faktorial (a) / faktorial (c)
    print (hasil)

#Kombinasi
a = 5
b = 3
print('Kombinasi dari (5 , 3) = ', end = ' '), kombinasi (5, 3)

#Permutasi
a = 10
b = 7
print('Permutasi dari (10 , 7) = ', end = ' '), permutasi (10, 7)

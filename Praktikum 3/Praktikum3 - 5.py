#Praktikum3 no 5

from operation import *

#menampilkan hasil 2 + 4 * 6 - 4
a = kali(4 , 6)
b = jumlah(2 , a)
c = kurang(b , 4)
print('a. 2 + 4 * 6 - 4 = ', c)

#menampilkan hasil (4 + 7) * (6 - 9)
a = jumlah(4 , 7)
b = kurang(6 , 9)
c = kali(a , b)
print('b. (4 + 7) * (6 - 9) = ', c)

#menampilkan hasil (10 + 2)/(7 + 5)/(12 - 34)
a = jumlah(10 , 2)
b = jumlah(7 , 5)
c = kurang(12 , 34)
d = bagi(a , b)
e = bagi(d , c)
print('c. (10 + 2) / (7 + 5) / (12 - 34) = ', e)

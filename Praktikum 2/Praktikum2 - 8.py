#Praktikum2 no 8

def luasSegitiga(a , t):
    luas = a * t / 2
    return luas

alas = 10
tinggi = 20
print('Luas Segitiga dengan alas ', alas,
      ' dan tinggi ', tinggi,
      ' adalah ', luasSegitiga(10 , 20))
alas = 15
tinggi = 45
print('Luas Segitiga dengan alas ', alas,
      ' dan tinggi ', tinggi,
      ' adalah ', luasSegitiga(15 , 45))
print('Total luas kedua segitiga tersebut adalah ', luasSegitiga(10 , 20) + luasSegitiga(15 , 45))

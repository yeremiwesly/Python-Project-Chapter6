#Latihan 1

def isPythagoras (a, b, c):
    if(a * a) == (c * c) - (b * b) or (b * b) == (c * c) - (a * a) or (c * c) == (a * a) + (b * b):
        print(True)
    else:
        print(False)         

#a = 3, b = 4 , c = 5        
print ('a. a = 3, b = 4, c = 5  -> ', end = ' '), isPythagoras(3, 4, 5)

#a = 5, b = 9, c = 12
print('b. a = 5, b = 9, c = 12 -> ', end = ' '), isPythagoras(5, 9, 12)

#a=8, b=6, c=10
print('c. a = 8, b = 6, c = 10 -> ', end = ' '), isPythagoras(8, 6, 10)

#a=7, b=8, c=11
print('d. a = 7, b = 8, c = 11 -> ', end = ' '), isPythagoras(7, 8, 11)

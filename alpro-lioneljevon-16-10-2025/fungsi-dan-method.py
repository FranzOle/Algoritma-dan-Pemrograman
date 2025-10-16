#fungsi tidak berisi/void
def PrintNama(nama):
    print(f"Hello World {nama}")

def tambah(a, b):
    return a + b

def tambahTiga(a, b, c):
    return a + b + c

#name argumen dengan parameter opsional
def opsionalBelanja(belanja, diskon=0):
    total = belanja - (belanja * diskon)/100
    return total

c = tambah(2, 4)
print(c)
print(tambah(3, 5)) 
print(tambahTiga(2, 3, 4))

PrintNama("Lionel Jevon")

#contoh bolak balik
def kali(a, b):
    print("a adalah", a)
    print("b adalah", b)
    print("a * b adalah", a * b)

kali(b = 3, a = 4)

#anonymous function
x = lambda a : a + 10
print(x(5))

kali = lambda a, b : a * b
print(kali(2, 3))

#contoh lambda dengan fungsi

def fungsiLambda(x, y):
    return lambda a : a * x + y

hasil = fungsiLambda(2, 3)

print(hasil(4)) # 2*4 + 3 = 11
print(hasil(5)) # 2*5 + 3 = 13  

#double program 

def doubleLambda(n):
    return lambda a : a * n

hasilX = doubleLambda(2)
hasilY = doubleLambda(3)
print(hasilX(11)) # 2*11 = 22
print(hasilY(11)) # 3*11 = 33
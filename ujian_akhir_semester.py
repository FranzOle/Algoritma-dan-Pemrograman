#Soal Nomor 1.
a = 5
b = 10

a = b - a
b = b - a
a = b + a

print(f"a = {a}")
print(f"b = {b}")
print('\n')


#Soal Nomor 2.
a = True
b = False
c = False
d = True

if (a and b) or ((not c) and d):
    if ((a or not b) and c) or (b and (not a)):
        print(1)
    else:
        if (a or (d and b)) and (not b):
            print(2)
        else:
            print(4)
else:
    if not (d and c) and (not a):
        print(5)
        print('\n')
    else:
        print(6)
        print('\n')
    print('\n')
    
#Maka Jawabannya: 2 

#Soal Nomor 3.
count = 0

def hitungsaja(n, m):
    global count
    if n < m:
        count += 1
        print(f"{count}. hello")
        k = (m + n) // 2
        hitungsaja(n, k)
        hitungsaja(k + 1, m)
    else:
        count += 1
        print(f"{count}. hello")

hitungsaja(1, 4)
print('\n')
#Maka Jawabannya: 7

#Soal Nomor 4.
j = 2
for i in range(0, 11):
    if j > 0:
        print("ok")
    j = 5 - (j * 2)

print(f"Nilai akhir j: {j} \n" )
#Maka Jawabannya: Nilai akhir j: -681

#Soal Nomor 5.
x = 10
y = 10

x = x * x
y = x

if x < y:
    x = y - 1
elif x > y:
    x = y + 1
else:
    x = x // x

print(f"Nilai akhir x adalah: {x} \n")
#Maka Jawabannya: Nilai akhir x adalah: 1

#Soal Nomor 6.
a = False
b = False
c = True

#b dan c boleh bernilai apa saja silahkan diubah ntuk testing

if (a and not (not c and not b)) or not ((c and b) or not a):
    print("ding")
else:
    print("dong")
print('\n')
#Maka Jawabannya: Mencetak 'dong' apapun nilai variabel b dan variabel c

#Soal Nomor 7.
count = 0

for x in range(100, 1001):
    if x % 3 == 0 and x % 5 == 0 and x % 30 != 0:
        count += 1

print(count)
#Maka Jawabannya: 30

#Soal Nomor 8.
n = 20
i = 0

while i < n:
    i = i + 4
    if i < n:
        for j in range(4):
            print('*', end='')
    print('\n')
#Maka Jawabannya: Mencetak 4 baris bintang dengan 4 bintang pada setiap barisnya. maka jawabannya adalah 16

#Soal Nomor 9.
P = False
Q = True

hasil = not (not (P or not Q) or (not P and not Q)) or (P or not Q)
print(hasil, "\n")
#Maka Jawabannya: P = False, Q = True, hasil = False

#Soal Nomor 10.
def wow(x):
    if x < 2:
        return x
    else:
        return wow(x - 2) + 3 * wow(x - 1)

print(wow(8), "\n")
#Maka Jawabannya: 3927

#Soal Nomor 11.
P = True
Q = False

asli = (P and (Q or P)) and (not Q or (P and not Q))
opsi = P and not Q

print(asli)
print(opsi)
print('\n')
#Maka Jawabannya: asli = True, opsi = True dengan demikian P and not(Q)

#Soal Nomor 12.
ans = 0
x = 80

for i in range(1, x + 1):
    if i % 3 == 0:
        ans += 1

print(ans)
print('\n')
#Maka Jawabannya: 26

#Soal Nomor 13.
merpati = 2018

if merpati % 100 > 20:
    merpati = merpati + 1
else:
    merpati = merpati + 2

print(merpati + merpati)
print('\n')
#Maka Jawabannya: 4040

"""
Soal Nomor 14.
F < A (F sebelum A)

B < D (B sebelum D)

B < E (B sebelum E)

C < B (C sebelum B)

A < B (A sebelum B)

Jawaban: F, A, C, B, E, D"""

#Soal Nomor 15.
n = 14934976

while n >= 10:
    temp = 1
    while n > 0:
        temp = temp * (n % 10)
        n = n // 10
    n = temp

print(n)
#Maka Jawabannya: 8
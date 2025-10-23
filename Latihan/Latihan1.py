# soal 1
alas = float(input("Masukkan Alas Segitiga" )) 
tinggi = float(input("Masukkan Tinggi Segitiga")) 
luas = 0.5 * (alas * tinggi) 
print(f"Luas Segitiga = {luas}" ) 

# soal 2:
bil = int(input("Masukkan Nomor Berapapun"))
if bil%2 == 0: 
    print("Bilangan Genap") 
else:
    print("Bilangan Ganjil")
    
#soal 3:
n = int(input("Masukkan n: "))

i = 1
total = 0

while i <= n:
    total = total + i
    i += 1

print(total)

#soal 4
data = input("Masukkan beberapa nilai (pisahkan dengan spasi): ").split()
angka = [int(x) for x in data]

print("Nilai tertinggi:", max(angka))
print("Nilai terendah:", min(angka))

#soal 5 sama seperti 7

#soal 6
def fungsi_pertambahan(a, b):
    return int(a + b)
    
a = int(input("Masukkan a: "))
b = int(input("Masukkan n: "))
tambah = fungsi_pertambahan(a, b)
print("fungsi tambah adalah:", tambah)

#soal 7
def faktorial(n):
    if n == 0:
        return 1
    else:
        return n * faktorial(n -1)
        
n = int(input("Masukkan Faktorial"))
print(f"Faktorial dari {n} adalah {faktorial(n)}")

#soal 8
def rata_rata(num):
    sum = 0
    for i in range(len(num)):
        sum = sum + float(num[i])
        
    return sum/len(num)
    
num = input("Masukkan Berapapun Angka: ").split()
    
rata = rata_rata(num)
print(rata)

# soal 9

def is_palindrome(huruf):
    ref = huruf[::-1]
    
    if huruf == ref:
        print("Palindrom")
    else:
        print("bukan Palindrome")
        
huruf = str(input("Masukkan huruf"))
is_palindrome(huruf)
    
#Soal 10
def fibonacci(n):
    return fibonacci(n-1) + fibonacci(n-2)
    
n = int(input("Masukkan Nilai n: "))
print(fibonacci(n))

    
    
    
    
    
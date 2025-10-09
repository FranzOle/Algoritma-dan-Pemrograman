a = int(input("Masukkan angka pertama: "))
b = int(input("Masukkan angka kedua: "))

i = a
n = 0
sum = 0
while a <= b:
    if a % 2 != 0:
        print(a, end=" ")
        n = n + 1
        sum += a
    a += 1

print("Jumlah bilangan ganjil dari", i, "sampai", b, "adalah:", sum)
print("Banyak bilangan ganjil dari", i, "sampai", b, "adalah:", n)
print("rata-rata bilangan ganjil dari", i, "sampai", b, "adalah:", sum/n)
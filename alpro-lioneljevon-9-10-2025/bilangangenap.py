print("\n=================================")
print("\n")
print("Mencari Bilangan Genap \n")
awal = int(input("Masukkan Angka awal: "))
akhir_input = int(input("Masukkan Angka awal: "))

while awal <= akhir_input:
    awal += 1
    if awal%2 == 0:
        print("%d \t|" %(awal))


print("\n")
print("=======================\n")

print("Versi Metode For")
print("\n=================================")
print("\n")
print("Mencari Bilangan Genap \n")
awal = int(input("Masukkan Angka awal: "))
akhir_input = int(input("Masukkan Angka awal: "))

for awal in range(akhir_input+1):
    if awal % 2 == 0:
        print("%d \t|" % (awal))

print("\n")
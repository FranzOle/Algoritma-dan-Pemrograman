print("\n")
print("=======================\n")

x = int(input("Masukkan Start Perulangan: "))
akhir = int(input("Masukkan Akhir Perulangan: "))

print("\n=================================")
print("x \t| x+2 \t| x*x \t| (x+2)*x**2")

while x <= akhir:
    a = x + 1
    b = x + 2
    c = x * x
    d = (x + 2) * x ** 2
    print("%d \t| %d \t| %d \t| %d \t|"%(a, b, c, d))
    x += 1

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

x = int(input("Masukkan Start Perulangan: "))
akhir = int(input("Masukkan Akhir Perulangan: "))

print("\n=================================")
print("x \t| x+2 \t| x*x \t| (x+2)*x**2")

for x in range(akhir + 1):
    a = x + 1
    b = x + 2
    c = x * x
    d = (x + 2) * x ** 2
    print("%d \t| %d \t| %d \t| %d \t|" % (a, b, c, d))

print("\n=================================")
print("\n")
print("Mencari Bilangan Genap \n")
awal = int(input("Masukkan Angka awal: "))
akhir_input = int(input("Masukkan Angka awal: "))

for awal in range(akhir_input):
    if awal % 2 == 0:
        print("%d \t|" % (awal))

print("\n")
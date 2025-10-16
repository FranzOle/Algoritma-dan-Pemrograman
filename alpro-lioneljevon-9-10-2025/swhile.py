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

print("\n Versi Perulangan For")
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

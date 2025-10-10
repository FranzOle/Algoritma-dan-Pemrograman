print("TABEL PERKALIAN")


a = int(input("Masukkan angka pertama : "))
b = int(input("Masukkan angka kedua   : "))

print("\n📊 Hasil Tabel Perkalian dari", a, "sampai", b)
print("===================================================\n")

i = a
while i <= b:
    j = a
    while j <= b:
        print(f"{i:2} x {j:<2} = {i*j}", end="  ")
        j += 1
    print()
    i += 1

print("\n===================================================")




print("Menghitung Tarif PDAM \n")

pemakaian = int(input("Masukkan Pemakaian Air (dalam m3): "))

biaya = 0

if pemakaian <= 10:
    biaya = pemakaian * 5000
elif pemakaian <= 20:
    biaya = (10 * 5000) + ((pemakaian - 10) * 7500)
elif pemakaian <= 40:
    biaya = (10 * 5000) + (10 * 7500) + ((pemakaian - 20) * 10000)
else:
    biaya = (10 * 5000) + (10 * 7500) + (20 * 10000) + ((pemakaian - 40) * 15000)

print(f"Total Biaya PDAM: " "Rp {:,.0f}".format(biaya).replace(",", "."))
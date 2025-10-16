def tagihanListrik(pemakaian, golongan):
    biaya = 0
    if golongan == '1':
        if pemakaian <= 100:
            biaya = pemakaian * 1500
        else:
            biaya = 100 * 1500 + (pemakaian - 100) * 2000
    elif golongan == '2':
        if pemakaian <= 100:
            biaya = pemakaian * 2500
        else:
            biaya = 100 * 2500 + (pemakaian - 100) * 3000
    elif golongan == '3':
        if pemakaian <= 100:
            biaya = pemakaian * 4000
        else:
            biaya = 100 * 4000 + (pemakaian - 100) * 5000
    elif golongan == '4':
        if pemakaian <= 100:
            biaya = pemakaian * 5000
        else:
            biaya = 100 * 5000 + (pemakaian - 100) * 7000
    elif not golongan: 
        if pemakaian <= 100:
            biaya = pemakaian * 4000
        else:
            biaya = 100 * 4000 + (pemakaian - 100) * 5000

    return biaya


print("Menghitung Tagihan Listrik \n")

pemakaian = int(input("Masukkan Pemakaian Listrik (dalam kWh): "))
golongan = input("Masukkan Golongan (1, 2, 3, dan 4): ")

tagihan = tagihanListrik(pemakaian, golongan)

print(f"Total Tagihan Listrik: Rp {tagihan:,.0f}".replace(",", "."))

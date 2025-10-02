print("Program Menghitung Segitiga \n")

while True:
    alas = float(input("Masukkan alas: "))
    tinggi = float(input("Masukkan Tinggi: "))

    luas_segitiga = 0.5 * alas * tinggi

    print(f"Luas Segitiga adalah: {luas_segitiga} \n")
    lanjut = str(input("Lanjut (Ketik 0 untuk break): "))

    if lanjut == "0":
        break
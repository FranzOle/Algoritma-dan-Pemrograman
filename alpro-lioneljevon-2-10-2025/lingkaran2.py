print("Menghitung Luas & Keliling Lingkaran \n")

while True:
    phi = 3.14
    r = float(input("Masukkan jari-jari lingkaran: "))

    if r < 0:
        print("Tidak Bisa \n")

    else:
        luas = phi * r * r
        keliling = 2 * phi * r

        print(f"Luas lingkaran: {luas}")
        print(f"Keliling lingkaran: {keliling}\n")
        break
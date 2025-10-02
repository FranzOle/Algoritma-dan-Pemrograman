print("Menghitung Luas & Keliling Lingkaran \n")

while True:
    print("1 untuk luas 2 untuk keliling \n")
    count = str(input("Masukkan 1 atau 2: "))

    if count == "1":
        print("Menghitung Luas")
        while True:
            jari = float(input("Masukkan Jari-Jari: "))
            if jari < 0:
                print("Jari-jari tidak boleh negatif, silakan ulangi input.")
            else:
                break
        if jari % 7 == 0:
            luas = 22 / 7 * jari * jari
        else:
            luas = 3.14 * jari * jari
        print(f"Luas Lingkaran adalah: {luas} \n")

    elif count == "2":
        print("Menghitung Keliling")
        while True:
            jari = float(input("Masukkan Jari-Jari: "))
            if jari < 0:
                print("Jari-jari tidak boleh negatif, silakan ulangi input.")
            else:
                break
        if jari % 7 == 0:
            keliling = 2 * 22 / 7 * jari 
        else:
            keliling = 2 * 3.14 * jari
        print(f"Keliling Lingkaran adalah: {keliling} \n")

    lanjut = str(input("Lanjut (Ketik 0 untuk break): "))
    if lanjut == "0":
        break

print("Menghitung jumlah hari dalam sebuah bulan di tahun 2020")

hari = 0
while True:
    bulan = int(input("Masukkan bulan (1-12): "))

    if bulan >= 1 and bulan <= 12:
        if bulan == 2:
            hari = 29
        elif not bulan % 2 == 0 and bulan <= 7:     
            hari = 31
        elif bulan % 2 == 0 and bulan <= 7:         
            hari = 30
        elif bulan % 2 == 0 and bulan > 7:          
            hari = 31
        elif not bulan % 2 == 0 and bulan > 7:     
            hari = 30
        print(f"Bulan ke-{bulan} pada tahun 2020 memiliki {hari} hari")
        break

    else:
        print("Bulan yang dimasukkan tidak valid masukkan angka antara 1 hingga 12.")
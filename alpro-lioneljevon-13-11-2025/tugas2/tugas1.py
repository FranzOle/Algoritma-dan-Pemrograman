# Jumlah data
jmlData = int(input("Masukkan jumlah data: "))

aplikasi = {}

for i in range(jmlData):
    data = input(f"Data {i+1}: ").strip()
    nama, kategori = data.split(',')
    nama = nama.strip()
    kategori = kategori.strip()

    if nama not in aplikasi:
        aplikasi[nama] = set()
    
    aplikasi[nama].add(kategori)

KategoriAll = set()
for i in aplikasi.values():
    KategoriAll.update(i)

kategori1 = []
for nama, setKategori in aplikasi.items():
    if len(setKategori) == 1:
        kategori1.append(nama)

kategori2 = []
if len(KategoriAll) > 2:
    for nama, setKategori in aplikasi.items():
        if len(setKategori) == 2:
            kategori2.append(nama)

print("Aplikasi yg muncul di 1 kategori:")
for a in sorted(kategori1):
    print(a)

if len(KategoriAll) > 2:
    print("Aplikasi yg muncul di 2 kategori:")
    for a in sorted(kategori2):
        print(a)

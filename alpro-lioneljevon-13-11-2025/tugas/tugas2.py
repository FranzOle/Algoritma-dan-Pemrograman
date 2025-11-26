dataMhasiswa = ('Lionel Jevon', '250091397019', 'Rungkut, Surabaya')

nama_lengkap = dataMhasiswa[0]
nim = dataMhasiswa[1]
alamat = dataMhasiswa[2]

print(f"Data: {dataMhasiswa}")
print()

print("Nim : ", nim)
print("Nama : ", nama_lengkap)
print("Alamat : ", alamat)

nimdigit = tuple(nim)
print("Nim: ", nimdigit)

namaKata = nama_lengkap.split()
namaDepan = namaKata[0]
namaDepan = tuple(namaDepan.lower())
print("Nama Depan:", namaDepan)

namaTerbalik_list = namaKata[::-1]
namaTerbalik_tuple = tuple(namaTerbalik_list)
print("Nama Yang Terbalik:", namaTerbalik_tuple)
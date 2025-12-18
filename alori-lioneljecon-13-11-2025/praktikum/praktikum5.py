n = int(input('Masukkan jumlah kategori: '))
# siapkan dictionary kosong
data_aplikasi = {}
for i in range(n):
    nama_kategori = input('Masukkan nama kategori:')
    print('Masukkan 5 nama aplikasi di kategori', nama_kategori)

aplikasi = []
for j in range(5):
    nama_aplikasi = input('Nama aplikasi: ')
    aplikasi.append(nama_aplikasi)

data_aplikasi[nama_kategori] = aplikasi

print(data_aplikasi)
daftar_aplikasi_list = []

for aplikasi in data_aplikasi.values():
    daftar_aplikasi_list.append(set(aplikasi))
    
print(daftar_aplikasi_list)

hasil = daftar_aplikasi_list[0]
for i in range(1, len(daftar_aplikasi_list)):
    hasil = hasil.intersection(daftar_aplikasi_list[i])
print(hasil)
kalimat = 'Manajemen Informatika UNESA'
print(f'Panjang Kalima: ,%d {len(kalimat)}')  # Menghitung panjang string
print(kalimat)
print(kalimat[0])  # Mengakses karakter pertama
print(kalimat[11])  # Mengakses karakter ke-12
print(kalimat[-1])  # Mengakses karakter terakhir

while i < len(kalimat):
    print(f'Karakter ke-{i} : {kalimat[i]}')
    i += 1
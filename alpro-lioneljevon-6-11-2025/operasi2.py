filename = input("Masukkan nama file: ")
handle = open(filename)
c = 0

for line in handle:
    if line.find('data.txt') != -1:
        c += 1
        print('file ditemukan pada baris ke-'+ line.strip() + "\"")

print("Jumlah kemunculan kata 'data.txt': ", c)
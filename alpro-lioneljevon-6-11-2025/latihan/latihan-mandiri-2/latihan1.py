f1 = open('file1.txt')
f2 = open('file2.txt')

isi1 = f1.readlines()
isi2 = f2.readlines()

f1.close()
f2.close()

maks = max(len(isi1), len(isi2))

for i in range(maks):
    baris1 = isi1[i].strip() if i < len(isi1) else ""
    baris2 = isi2[i].strip() if i < len(isi2) else ""
    if baris1 != baris2:
        print("Perbedaan pada baris ke: ", i+1)
        print("file 1: ", baris1)
        print("filw 2: ", baris2)

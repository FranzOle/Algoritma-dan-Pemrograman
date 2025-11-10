import re
from collections import Counter

def duplikasi_kata(text, kata_find):
    text = text.lower()
    kata_find = kata_find.lower()
    daftar_kata = re.findall(r'\b\w+\b', text)
    angka_kata = Counter(daftar_kata)

    duplicates = {word: count for word, count in angka_kata.items() if count > 1}

    jumlah = angka_kata.get(kata_find, 0)

    return duplicates, jumlah

teks = str(input("Masukkan kata-kata: "))
tekscar = str(input("Dari kata-katamu, kata apa yang mau kamu cari: "))

duplicates, jumlah_kata = duplikasi_kata(teks, tekscar)

print("Jumlah kata yang kamu cari adalah: ", jumlah_kata)
print("Kata-kata yang duplikat: ", duplicates)

kalimat = input("Masukkan kalimat: ")

kata_kata = kalimat.split()

terpendek = min(kata_kata, key=len)
terpanjang = max(kata_kata, key=len)

print("Kata terpendek:", terpendek)
print("Kata terpanjang:", terpanjang)
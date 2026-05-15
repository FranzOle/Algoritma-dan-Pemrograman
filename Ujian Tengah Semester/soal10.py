# Inisialisasi variabel contoh
a = 2
b = 4
c = 6
d = 3
x = 5
y = 1
r = 10

print("== Ekspresi Matematika dalam Python ==\n")

# a. (3 + 4x)/5 - [10(y - 5)(a + b + c)]/x + 9(4/x + (9 + x)/y)
# Catatan: Tanda kurung sangat penting untuk memisahkan pembilang dan penyebut.

ekspresi_a = (3 + 4 * x) / 5 - (10 * (y - 5) * (a + b + c)) / x + 9 * ((4 / x) + ((9 + x) / y))
print("a. Hasil ekspresi a:", ekspresi_a)

# b. 4/[3(r + 34)] - 9(a + bc) + [3 + d(2 + a)]/(a + bd)

ekspresi_b = 4 / (3 * (r + 34)) - 9 * (a + b * c) + (3 + d * (2 + a)) / (a + b * d)
print("b. Hasil ekspresi b:", ekspresi_b)

print("Menghitung Persamaan Matematika \n")

a = int(input("Masukkan nilai a: "))

f = lambda x: 2*x**3 + 2*x + 15/x

print("Hasil dari f(", a, ") adalah:", f(a))
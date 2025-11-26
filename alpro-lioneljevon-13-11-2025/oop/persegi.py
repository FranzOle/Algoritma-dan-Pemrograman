class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def luas(self):
        return self.panjang * self.lebar

    def keliling(self):
        return 2 * (self.panjang + self.lebar)


try:
    panjang = float(input("Masukkan panjang: "))
    lebar = float(input("Masukkan lebar: "))
except ValueError:
    print("Input harus angka.")
    exit()

persegi = PersegiPanjang(panjang, lebar)

print("Luas persegi panjang:", persegi.luas())
print("Keliling persegi panjang:", persegi.keliling())

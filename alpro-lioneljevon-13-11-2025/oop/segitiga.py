class Segitiga:
    #konstruktor
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def hitung_luas(self):
        return 0.5 * self.alas * self.tinggi
    
alas = int(input("Masukkan alas : "))
tinggi = int(input("Masukkan tinggi : "))

segitiga = Segitiga(alas, tinggi)
print("Luas: ", segitiga.hitung_luas())
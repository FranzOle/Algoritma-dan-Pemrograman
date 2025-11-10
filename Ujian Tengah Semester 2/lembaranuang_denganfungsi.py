print("Menghitung pecahan uang dari kelipatan 500 dengan fungsi \n")

uang = int(input("Masukkan jumlah uang kelipatan 500: "))

def menghitung_lembaran_uang(uang):
    if uang % 500 != 0:
        return None
    
    else:
        sisa = uang
        lembar_50k = sisa // 50000
        sisa = sisa % 50000
        lembar_20k = sisa // 20000
        sisa = sisa % 20000

        lembar_10k = sisa // 10000
        sisa = sisa % 10000

        lembar_5k = sisa // 5000
        sisa = sisa % 5000

        lembar_1k = sisa // 1000
        sisa = sisa % 1000

        lembar_500 = sisa // 500

    return lembar_50k, lembar_20k, lembar_10k, lembar_5k, lembar_1k, lembar_500

print("Lembaran uang 50.000 :", menghitung_lembaran_uang(uang)[0], "lembar")
print("Lembaran uang 20.000 :", menghitung_lembaran_uang(uang)[1], "lembar")
print("Lembaran uang 10.000 :", menghitung_lembaran_uang(uang)[2], "lembar")
print("Lembaran uang 5.000  :", menghitung_lembaran_uang(uang)[3], "lembar")
print("Lembaran uang 1.000  :", menghitung_lembaran_uang(uang)[4], "lembar")
print("Lembaran uang 500    :", menghitung_lembaran_uang(uang)[5], "lembar")
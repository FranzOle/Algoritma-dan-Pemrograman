print("Rata Rata Bilangan Bulat \n")

bilangan1 = int(input("Masukkan bilangan bulat pertama: "))
bilangan2 = int(input("Masukkan bilangan bulat kedua: ")) 
bilangan3 = int(input("Masukkan bilangan bulat ketiga: "))

rataRata = lambda a, b, c: (a + b + c) / 3

print("Rata-rata dari", bilangan1, ",", bilangan2, "dan", bilangan3, "adalah:", rataRata(bilangan1, bilangan2, bilangan3))
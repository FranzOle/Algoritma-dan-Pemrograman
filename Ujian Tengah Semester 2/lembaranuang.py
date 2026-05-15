print("Menghitung pecahan uang \n")

uang = int(input("Masukkan jumlah uang yg kelipatan 500: "))

if not uang % 500 == 0:
    print("Jumlah uang harus kelipatan 500.")

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

print(f"Pecahan 50.000 : {lembar_50k} lembar")
print(f"Pecahan 20.000 : {lembar_20k} lembar")
print(f"Pecahan 10.000 : {lembar_10k} lembar")
print(f"Pecahan 5.000  : {lembar_5k} lembar")
print(f"Pecahan 1.000  : {lembar_1k} lembar")
print(f"Pecahan 500   : {lembar_500} lembar")

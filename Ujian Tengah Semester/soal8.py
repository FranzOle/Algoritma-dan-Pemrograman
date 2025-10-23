x_input = int(input("Masukkan nilai X: "))
y = int(input("Masukkan nilai Y: "))
hasil = 0
x = x_input

while x > 0:
    if x % 2 == 1:
        hasil = hasil + y
    
    x = x // 2
    y = y * 2

print("Hasil =", hasil)
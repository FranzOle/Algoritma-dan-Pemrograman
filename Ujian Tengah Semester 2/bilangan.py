total = 0
bilangan = float(input("Masukkan bilangan ke 1: "))
tertinggi = bilangan
terendah = bilangan
total += bilangan

for i in range(2, 6):
    bilangan = float(input(f"Masukkan bilangan ke {i}: "))
    total += bilangan
    if bilangan > tertinggi:
        tertinggi = bilangan
    if bilangan < terendah:
        terendah = bilangan

rata = total / 5

print("Nilai trtinggi :", tertinggi)
print("Nilai terendah  :", terendah)
print("Nilai rata rata :", rata)

t = tuple(map(int, input("Masukkan angk angka : ").split()))

sama = True
first = t[0]

for item in t:
    if item != first:
        sama = False
        break

if sama:
    print("Semua Tuple bernilai sama")
else:
    print("Tuple ada yang tidak sama")

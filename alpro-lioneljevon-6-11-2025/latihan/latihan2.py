import re

tgl = "2025-11-06"
hasil = tgl.split("-")
tgl2 = hasil[2]+"-"+hasil[1]+"-"+hasil[0]
print(tgl2)

tglInput = str(input("Input Tanggalan"))
hasil = re.split("[-,/ ]+",tglInput)
print(hasil)
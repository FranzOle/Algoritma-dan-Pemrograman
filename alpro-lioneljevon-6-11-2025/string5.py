kalimat = "Saudara-Saudara pada tanggal 17-08-1945 indonesia merdeka"
hasil = kalimat.split(" ")
print(hasil[0])  # Output: Saudara-Saudara
print(hasil[1])  

tgl = hasil[3]
tglsplit = tgl.split("-")
tglBaru = tglsplit[0] + "/" + tglsplit[1] + "/" + tglsplit[2]
print(tglBaru)  
print(hasil[0]+ " "+ hasil[1]+ " "+ hasil[2] + "" + tglBaru + " " + hasil[4].capitalize()+ " "+ hasil[5].upper())

for kal in hasil:
    if kal[0].isdigit():
        hasil2 = kal.split("-")
        print(hasil2[0]+ "/" + hasil2[1]+ "/" + hasil2[2])

str1 = 'unesa'
str2 = 'Unesa'
str3 = 'UNESA'
str4 = ' UnEsA'

print(str1 == str2.lower())  # True
print(str2 == str3.capitalize())  # True
print(str3 == str4.strip().upper())  # True
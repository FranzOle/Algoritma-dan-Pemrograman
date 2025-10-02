print("Perhitungan Tunjangan Karyawan\n")
nama = input("Masukkan nama karyawan: ")
gaji_pokok = 0
gaji_pokok = float(input("Masukkan gaji pokok: "))
golongan = int(input("Masukkan golongan (1/2/3): "))
pendidikan = int(input("Masukkan pendidikan (SMA = 1, D4/S1 = 2, S2 = 3, S3 = 4): "))
jam_kerja = float(input("Masukkan jam kerja dalam sebulan: "))

tunjangan_golongan = 0
tunjangan_pendidikan = 0
tunjangan_lembur = 0

if golongan == 1:
    tunjangan_golongan = 0.05 * gaji_pokok
elif golongan == 2: 
    tunjangan_golongan = 0.1 * gaji_pokok
elif golongan == 3:
    tunjangan_golongan = 0.15 * gaji_pokok

if pendidikan == 1:
    tunjangan_pendidikan = 0.05 * gaji_pokok
elif pendidikan == 2:
    tunjangan_pendidikan = 0.1 * gaji_pokok
elif pendidikan == 3:
    tunjangan_pendidikan = 0.2 * gaji_pokok
elif pendidikan == 4:
    tunjangan_pendidikan = 0.3 * gaji_pokok

jam_harian = 8
hari_kerja = 24
jam_normal_per_bulan = jam_harian * hari_kerja
jam_lembur = jam_kerja - jam_normal_per_bulan
tunjangan_lembur = jam_lembur * 3500

gaji_total = gaji_pokok + tunjangan_golongan + tunjangan_pendidikan + tunjangan_lembur

print("\nRincian Gaji Karyawan:")
print(f"Nama Karyawan: {nama}")
print(f"Gaji Pokok: {gaji_pokok}")
print(f"Tunjangan Golongan: {tunjangan_golongan}")
print(f"Tunjangan Pendidikan: {tunjangan_pendidikan}")
print(f"Tunjangan Lembur: {tunjangan_lembur}")
print(f"Total Gaji: {gaji_total}")

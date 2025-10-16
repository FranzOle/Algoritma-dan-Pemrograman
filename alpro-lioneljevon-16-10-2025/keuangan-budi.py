print("=== Program Perhitungan Keuangan Budi Selama Liburan ===\n")

gaji_per_jam = float(input("Masukkan gaji per jam (Rp): "))
jam_minggu = float(input("Masukkan jumlah jam kerja per minggu: "))

def pendapatan_budi(gaji, jam):
    pendapatan_kotor = gaji*jam * 5
    pajak = 0.14 * pendapatan_kotor
    pendapatan_bersih = pendapatan_kotor - pajak
    return pendapatan_kotor, pajak, pendapatan_bersih

def pengeluaran_budi(pendapatan_bersih):
    pengeluaran_baju = 0.1 * pendapatan_bersih
    pengeluaran_alat_tulis = 0.01 * pendapatan_bersih
    sisa_belanja = pendapatan_bersih - (pengeluaran_baju + pengeluaran_alat_tulis)
    return pengeluaran_baju, pengeluaran_alat_tulis, sisa_belanja

def sedekah_budi(sisa_belanja):
    sedekah = 0.25 * sisa_belanja
    sedekah_yatim = 0.3 * sedekah
    sedekah_dhuafa = sedekah - sedekah_yatim
    return sedekah, sedekah_yatim, sedekah_dhuafa

pendapatan_kotor, pajak, pendapatan_bersih = pendapatan_budi(gaji_per_jam, jam_minggu)
pengeluaran_baju, pengeluaran_alat_tulis, sisa_belanja = pengeluaran_budi(pendapatan_bersih)
sedekah, sedekah_yatim, sedekah_dhuafa = sedekah_budi(sisa_belanja)

print("\nRincian Keuangan Budi ")
print(f"Pendapatan Kotor: Rp {pendapatan_kotor:,.0f}".replace(",", ".") )
print(f"Pajak (14%): Rp {pajak:,.0f}".replace(",", ".") )
print(f"Pendapatan Bersih: Rp {pendapatan_bersih:,.0f}".replace(",", ".") )
print(f"Pengeluaran untuk Baju: Rp {pengeluaran_baju:,.0f}".replace(",", ".") )
print(f"Pengeluaran untuk Alat Tulis: Rp {pengeluaran_alat_tulis:,.0f}".replace(",", ".") )
print(f"Sisa Belanja: Rp {sisa_belanja:,.0f}".replace(",", ".") )
print(f"Total Sedekah (25% dari Sisa Belanja): Rp {sedekah:,.0f}".replace(",", ".") )
print(f"  - Sedekah untuk Anak Yatim (30% dari Total Sedekah): Rp {sedekah_yatim:,.0f}".replace(",", ".") )
print(f"  - Sedekah untuk Dhuafa: Rp {sedekah_dhuafa:,.0f}".replace(",", ".") )

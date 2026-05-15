def hapus_spasi_berlebih(teks):
    return " ".join(teks.split())

kalimat = "saya   tidak   suka   memancing ikan   "
hasil = hapus_spasi_berlebih(kalimat)

print("Output:", hasil)
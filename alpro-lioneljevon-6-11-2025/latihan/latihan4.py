text = 'A quick brown fox jumps over the lazy dog.'
def ambil_kata_kalimat(kalimat, n):
    kalimat = kalimat.lower() 
    hasil_akhir = []
    hasil = kalimat.split() 
    for i in range (0,len(hasil)):
        tmp = ' '.join(hasil[i:i + n])
        hasil_akhir.append(tmp)

    return hasil_akhir #return

print(ambil_kata_kalimat(text, 2))
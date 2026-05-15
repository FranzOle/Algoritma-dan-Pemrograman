print("Cek Duplikat")

def cek_duplikat(string):
# buat set kosong
    karakter_set = set()

    for karakter in string:
    # apakah karakter ini ada dalam set?
        if karakter in karakter_set:
            return True
        else:
            karakter_set.add(karakter)
            return False
# test case
string1 = 'Alexander the Great' # duplikat
print(cek_duplikat(string1))
string2 = 'UNESA' # semua unik
print(cek_duplikat(string2))

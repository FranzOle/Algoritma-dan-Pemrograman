def anagram(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()

    if sorted(s1) == sorted(s2):
        return True
    else:
        return False
    
s1 = str(input("Masukkan kata pertama: "))
s2 = str(input("Masukkan kata ke dua: "))

benar = anagram(s1, s2)
status = ""
if benar == True:
    status = "Benar"
else:
    status = "Salah"

print("Apakah Kedua Kata Tersebut adalah anagram: ", status)
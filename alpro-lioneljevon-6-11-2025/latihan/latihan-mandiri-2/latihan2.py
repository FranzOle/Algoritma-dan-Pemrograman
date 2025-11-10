print("nama file1: soal.txt\n")

f = open('soal.txt', 'r', encoding='utf-8')
lines = f.readlines()
f.close()

for line in lines:
    line = line.strip()
    if not line:
        continue  

    if '||' in line:
        parts = line.split('||', 1)
        soal = parts[0].strip()
        jawaban_benar = parts[1].strip()
    else:
        soal = line
        jawaban_benar = ""

    print(soal)
    jawaban_user = input("Jawab: ").strip()
    if jawaban_user.lower() == jawaban_benar.lower():
        print("Jawaban benar!\n")
    else:
        print("Jawaban salah!\n")

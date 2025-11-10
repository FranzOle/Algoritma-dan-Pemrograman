a_string = "AnTonIus"
lowercase = a_string.lower()
total = 0
for x in "aiueo":
    jml = lowercase.count(x)
    total += jml
# untuk mencari huruf aiueo
print(total)
#hasil = 4

b_string = "dInO Arsaka AirlAnggA"
lowercase = b_string.lower()
total1 = 0
i = 0
vokal = "aiueo"
while i < len(vokal):
    huruf = vokal[i]
    jml1 = lowercase.count(huruf)
    total1 += jml1
    i = i + 1
    
print(total1)
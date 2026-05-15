fname = input("Enter a file name: ")

f = open(fname)
counts = {}

for line in f:
    line = line.rstrip()
    if line.startswith('From '):
        parts = line.split()
        waktu = parts[5]        
        jam = waktu.split(':')[0]  
        
        if jam not in counts:
            counts[jam] = 1
        else:
            counts[jam] += 1

jam_urut = list(counts.items())
jam_urut.sort()

for jam, total in jam_urut:
    print(jam, total)

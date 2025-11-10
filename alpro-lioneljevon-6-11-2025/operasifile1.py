handle = open(r'C:\Users\ASUS\OneDrive\Documents\GitHub\Algoritma-dan-Pemrograman\alpro-lioneljevon-6-11-2025\data.txt', 'r')
print(handle.read())

i = 0

for line in handle:
    i+=1
print("Jumlah baris: ", i)
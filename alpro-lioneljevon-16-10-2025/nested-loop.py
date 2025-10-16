print("Studi Kasus Nested Loop \n")

print("Segitiga Angka")
n = int(input("Masukkan jumlah baris: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()


for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(i, end=' ')   
    print()

print("Baris angka")

for i in range(1,n+1):
    if i%2==1:
        for j in range(1,n+1):
            print(j," ",end='')
    else:
        for j in range(n,0,-1):
            print(j," ",end='')
    print()
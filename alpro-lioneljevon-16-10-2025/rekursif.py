print("Fungsi Rekursif dan Faktorial \n")

def hitung_mundur(n):
    if n == 0:               
        print("Selesai!")
    else:
        print(n)
        hitung_mundur(n - 1)  

hitung_mundur(5)

def faktorial(n):
    if n == 0 or n == 1:     
        return 1
    else:
        return n * faktorial(n - 1)
    
print("Faktorial dari 5 adalah:", faktorial(5))
print("Faktorial dari 7 adalah:", faktorial(7))

def rekursif(x, y):
    if y == 1:
        return x
    else:
        return x * rekursif(x, y - 1)
    
print("Hasil dari 3^4 adalah:", rekursif(3, 4))

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
print(f"Fibonacci adalah {fibonacci(7)}")
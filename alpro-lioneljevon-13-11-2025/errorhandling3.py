try:
    num = int(input("Masukkan Angka"))
    assert num % 2 == 0
except:
    print('Bukan Even number')
else:
    reciprocal = 1/num
    print(reciprocal)

try:
    a = 10
    b = 0
    result = a/b
    print(result)
except:
    print('Error')
finally:
    print('Bisa bisa')


#finally akan dijalankan apapun kondisinya

    
try:
    even_numbers = [2,4,6,8]
    # print(even_numbers[5])

    a = 10
    b = 0
    print(a/b)
except ZeroDivisionError:
    print('Tidak Bisa Dibagi 0')
except IndexError:
    print('Out of bound')

    #tidak bisa dua kopondisi jadi kondisi teratas terpenuhi maka akan loc=ncat ke except seperti logika algoritmik
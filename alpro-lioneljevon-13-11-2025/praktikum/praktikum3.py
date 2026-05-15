print('Praktikum set')
def unique_sum(list):
    data_set = set(list)
    total = 0
    for data in data_set:
        total = total + data

    return total

contoh1 = [2, 4, 3, 2, 7, 8, 6, 4, 5, 5]
hasil1 = unique_sum(contoh1)
print(hasil1)
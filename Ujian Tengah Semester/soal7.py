n = 62792912
while n >= 10:
    temp = 1
    while n > 0:
        temp = temp * (n % 10)
        n = n // 10
    n = temp

print(temp)

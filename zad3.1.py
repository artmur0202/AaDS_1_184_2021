a = [6, 2, 9, 13, 1, 8, 4, -5, -11, -8, -2, -6]
i = -1
s = 0
while a[i] < 0:
    s+=a[i]
    i-=1
print("Сумма отрицательных чисел: ", s )
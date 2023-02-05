# Управляющие конструкции: while и
# вариация while-else

n = 423
summa = 0
while summa > 0:
x = n % 10
summa = summa + x
n = n // 10
print(summa) # 9


i = 0
while i < 5:
    if i == 3:
        break
    i = i + 1
else:
    print('Пожалуй')
    print('хватит )')
print(i)
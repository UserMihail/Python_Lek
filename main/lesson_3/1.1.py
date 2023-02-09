# Функции и модули

# Задание: Необходимо создать функцию sumNumbers(n), которая будет считать
# сумму всех элементов от 1 до n.
"""
def sumNumbers(n):
    summa = 0
    for i in range(1, n + 1):
        summa += i
    print(summa)

sumNumbers(6)
"""
# Или

# def sumNumbers(n):
#     summa = 0
#     for i in range(1, n + 1):
#         summa += i
#     return summa

# print(sumNumbers(3))

# Или

def sumNumbers(n):
    summa = 0
    for i in range(1, n + 1):
        summa += i
    return summa

a = sumNumbers(7)
print(a)
#Логические операции

# Кое-что ещё: is, is not, in, not in
# В Python мы можем выполнять следующие сравнения. Результатом чего будет либо
# True, либо False

a = 1 > 4
print(a) # False
a = 1 < 4 and 5 > 2
print(a) # True
a = 1 == 2
print(a) # False
18
a = 1 != 2
print(a) # True

# Можно сравнивать не только числовые значения, но и строки:

a = 'qwe'
b = 'qwe'
print(a == b) # True

# В Python можно использовать тройные и даже четверные неравенства:

a = 1 < 3 < 5 < 10
print (a) # True

# Сложные условия
# Сложные условия создаются с помощью логических операторов, таких как: and, or,
# not

if condition1 and condition2: # выполнится, когда оба условия окажутся верными
# operator

if condition3 or condition4: # выполнится, когда хотя бы одно из условий
окажется верным

# operator
n = int(input())
if n % 2 == 0 and n % 3 == 0:
print('Число кратно 6')
if n % 5 == 0 and n % 3 == 0:
print('Число кратно 15')

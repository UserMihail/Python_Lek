"""
n = None
print(n)

n = 1.89
print(n)

n = 'dfdf'
print(n)
  
n = 'dfdf'
print(type(n)) # (type)вывети тип данных

n = 'df\'df'    # ковычки внутри строки
print(n) 

n = 'df" gjgj "df'  # ковычки внутри строки
print(n)  
"""

# Кавычки в выводе
# a = 5
# b = 5.89
# c = 'Hello'

# print(a,'-',b,'-',c) # вывод через -

# a =5
# b = 5.89
# c = 'Hello'

# print(f"{a} - {b} - {c}") # вывод через -

# a =5
# b = 5.89
# c = 'Hello'

# print("{}-{}-{}".format(a,b,c)) # вывод через -


# Ввод данных

# a = input()
# print(a)

# print('Введие первую строку: ')  # переход на новую строку
# a = input()
# b = input("Введите второе число: ")  # без перехода

# print(a, '+', b, '=', a + b) # cложились не числа а строки


# меняем тип данных

# c = 5.89
# print(c)
# n = int(c) #с помощьу int првели к целому значению
# print(n)

# c = 5.89
# print(c)
# print(type(c))
# c = int(c) 
# print(c)
# print(type(c))

# c = 5.89
# print(c)    #сюда добавить строку не сможем, будет ошибка
# print(type(c))
# c = str(c) 
# print(c + '89')
# print(type(c))

# c = 1
# print(c)
# print(type(c))
# c = bool(c) 
# print(c)
# print(type(c))

#v = 'ddafdf'  # -строка
#v = int(v)   # -число (ошибка)

# print('Введие первую число: ')  
# a = int(input())
# b = int(input("Введите второе число: ")) 

# print(a, '+', b, '=', a+b)

# print('Введие первую число: ')  
# a = int(input())
# b = int(input("Введите второе число: ")) 

# print(a+b)


#Округление числa

# a = 5.89989
# b = 6.456451
# print(round(a*b, 3)) #оставили 3 цифры после точки

# a = 5.89989
# b = 6.456451
# print(round(a*b, 3))


#логические операции

# a = 1 > 4
# print(a)

# a = 1 < 4 and 5 > 2
# print(a)

# a = 1 == 2
# print(a)

# a = 1 != 2
# print(a)

# a = 'asdf'
# b = 'asdf'
# print(a == b)

# a = 1 < 3 < 5 < 10 
# print(a)
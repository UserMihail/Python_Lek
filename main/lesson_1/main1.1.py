# цыкл if else

# username = input('enter a name: ')
# if username == 'Маша':
#     print('Ура, это же МАША!')
# elif username == 'Марина':
#     print('Я так ждала Вас, Марина!')
# elif username == 'Ильнар':
#     print('Ильнар - топ')
# else:
#     print('Привет, ', username)

#цыкл while

# i = 0 
# while i < 5:
#     # if i == 3:
#     #     break
#     i = i + 1
# else:
#     print('Пожалуй')
#     print('хватит )')
# print(i)

# перменная флаг

# n = int(input())
# flag = True
# i = 2
# while flag:
#     if n % i == 0:
#         flag = False
#         print(i)
#     elif i > n // 2:
#         print(n)
#         flag = False
#     i += 1

# цыкл фор

#в строке
# a = 'qwerty'
# for i in a:
#     print(i)


# line  = ""
# for i in range(5):
#     line = ""
#     for j in range(5):
#         line += "*"
#     print(line)

# размер строки

#text = 'Съешь еще этих мяГкИх францухких булок'
#print(len(text)) #позволяет узнать размер строки
#print('еще' in text) #есть ли слово еще в строке?
#print(text.lower())  #переводит буквы в нижний регистр
#print(text.upper())  #переводит буквы в вверхний регистр
#print(text.replace('еще', 'ЕЩЕ'))  #меняет слово в строе. первое какое слово, 2е на какое слово

# text = 'cъешь ещё этих мягких французских булок'
# print(text[0])                          # с                  
# print(text[1])                          # ъ
# print(text[len(text)-1])                # к
# print(text[-5])                         # б
# print(text[:])                          # cъешь ещё этих мягких французских булок
# print(text[:2])                         # съ
# print(text[len(text)-2])                # ок
# print(text[2:9])                        # ешь ещё
# print(text[6:-18])                      # ещё этих мягких
# print(text[0:len(text):6])             # сеикакл
# print(text[::6])                       # сеикакл
text = text[2:9] + text[-5] + text[:2]  # ...





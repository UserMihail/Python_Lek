"""
Функция принимающая неограниченное кол-во
аргументов
"""

def sum_str(*args): # *-неограниченное кол-во аргументов
    res = " "
    for item in args:
        res += item
    return res

print(sum_str('a', 's', 'd', 'w')) 
print(sum_str('a', 's', 'd', 'w', 'dfdf')) 
# coding: UTF-8


# Easy, задача 1
# fruits = ('orange' , 'apple' , 'banana', 'melon')
# print(fruits)
# n = 1
# for fruit in fruits:
#     print(f" {n}. {fruit}")
#     print('{}. {}'.format(n, fruit))
#     n += 1


# Easy, задача 2
# a = ['a', 'b', 'c', 1, 2, 3]
# b = ['d', 'e', 'c', 1, 2, 5]
# a1 = set(a)
# b1 = set(b)
# c = a1 - b1
# print(c)


# Easy, задача 3
# d = [10, 31, 72, 23, 71, 82, 9]
# e = []
# for el in d:
#     if el % 2 == 0:
#         el /= 4
#     else:
#         el *= 2
#     e.append(el)
# print(d)
# print(e)


# Normal, задача  1
# import math
# spis = [2, -5, 8, 9, -25, 25, 4]
# spis_1 = []
# for eL in spis:
#     if eL > 0 and math.sqrt(eL) == int(math.sqrt(eL)):
#         eL = math.sqrt(eL)
#         spis_1.append(int(eL))
# print(spis_1)


# Normal, задача 2
# Представим, что в месяце 10 дней
# a = '02.11.2013'
# b = a.split('.')
# print (b)
# dd = int(b[0]) - 1
# mm = int(b[1]) - 1
# yy = int(b[2])
# print (dd, mm, yy)
# dict = dict(
#     d=['первое', 'второе', 'третье', 'четвертое', 'пятое', 'шестое', 'седьмое', 'восьмое', 'девятое', 'десятое'],
#     m=['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря'])
# den = dict['d'][dd]
# mes = dict['m'][mm]
# print(f'Сегодня {den} {mes} {yy} года')

# Normal, задача 3
# import random
# spis = []
# n = int(input('Введите длину списка'))
# for i in range(0,n):
#     spis.append(random.randint(-100,100))
# print(spis)


# Normal, задача 4
# a = [1, 2, 4, 5, 6, 2, 5, 2]
# b = []
# for i in a:
#     if i not in b:
#         b.append(i)
#     else:
#         pass
# print(a)
# print(b)
# c = []
# for i in a:
#     n = a.count(i)
#     if n == 1:
#         c.append(i)
# print(c)


# Hard, задача 1
# x = 2.5
# eq = 'y = -12x + 11111140.2121'
# eq_spis = eq.split(' ')
# k = int(eq_spis[2][:3])
# b = float(eq_spis[-1])
# y = k * x + b
# print(f'Для уравнения {eq} при х = {x}:  y = {y}')


# Hard, задача 2
# data = input('Введите дату в восьмизначном формате через точку')
# dat = data.split('.')
# dd = int(dat[0])
# mm = int(dat[1])
# yy = int(dat[2])
# yy2 = dat[2]
# if dd in range(1,32):
#     if mm in range(1, 13):
#         if len(yy2) ==4 and yy > 1 and yy <9999:
#             print('Дата введена корректно')
#         else:
#             print('Дата введена не  корректно')
#     else:
#         print('Дата введена не  корректно')
# else:
#     print('Дата введена не  корректно')


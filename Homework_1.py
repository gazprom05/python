# coding: UTF-8



print('Привет, жиртрест. Давай заполним анкету')
name = input('Как тебя зовут? ')
age = int(input('Сколько тебе лет?'))
weight = int(input('Сколько весишь?'))

if (age > 10) & (age  <= 30):
    if weight < 50:
        print(f' {name}, тебе  {age} лет, а ты весишь {weight}кг. Пора жрать!')
    elif  (weight >= 50) & (weight <= 90):
        print(f' {name}, тебе {age} лет, со своими {weight}кг ты в хорошей форме!')
    else:
        print(f' {name}, тебе {age} лет, а ты весишь {weight}кг. Пора худеть!')
elif (age >= 30) & (age <= 55):
    if weight < 50:
        print(f' {name}, тебе {age} лет, а ты весишь {weight}кг. Сходи к врачу, ты суховат!')
    elif (weight >= 50) & (weight <= 90):
        print(f' {name}, тебе {age} лет, со своими {weight}кг ты в хорошей форме!')
    else:
        print(f' {name}, тебе {age} лет, а ты весишь {weight}кг. Пора бы заняться скандинавской ходьбой! ')
elif (age > 55) & (age <= 90):
    if weight < 50:
        print(f' {name}, тебе {age} лет, а ты весишь {weight}кг. Ты суховат, но уже ничего не поделаешь. Смирись.')
    elif (weight >= 50) & (weight <= 100):
        print(f' {name}, тебе {age} лет, со своими {weight}кг ты в отличной форме, иди на грядку!')
    else:
        print(f' {name}, тебе {age} лет, а ты весишь {weight}кг. Поздно пить боржоми, смотри битву экстрасенсов! ')
else:
    print('Ты или труп или ребенок')

# Easy, задача 1
# a = 10
# b = 'привет'
# c = True
#
# print(a,b,c)
# b = input('Введите значение для переменной c')
# print(a,b,c)


# Easy, задача 2
# d = int(input('Введите любое число'))
# d = d + 2
# print(d)

# Easy, задача 3
# e = int(input('Склдько тебе лет?'))
# if e >17:
#     print('Доступ разрешен')
# else:
#     print('Извините, доступ с 18 лет')


# Normal, задача 1

# while True:
#     f = int(input('Введите число'))
#     if (f >0) and (f < 10):
#         f **= 2
#         print(f)
#         break
#     else:
#         print('Введите число от 1 до 9')

# Normal, Задача 2

# g = int(input('введите число'))
# h = int(input('введите другое число'))
# print(g, h)
# print('Меняем местами')
# g,h = h,g
# print(g,h)

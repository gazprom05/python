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


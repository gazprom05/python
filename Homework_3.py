# coding: UTF-8

# Easy, задача 1
def stroka(name, age, city):
    return f'{name}, {age} год, проживает в городе {city}'
a , b , c = 'Vasia' , 21 , 'Moscow'
ddd = stroka(a,b,c)
print(ddd)


# Easy, задача 2
def max_count(numbers2):
    max = 0
    for n in numbers2:
        if int(n) > max:
            max = n
    return max
numbers = [1 , 6 , 3]
max_number = max_count(numbers)
print(f'Самое большое число {max_number}')


# Easy, задача 3
def long_str(*stroki):
    max_dlin_stroki = 0
    for stroka in stroki:
            if len(stroka) > max_dlin_stroki:
                max_dlin_stroki = len(stroka)
                very_long_str = stroka
    return very_long_str
max = long_str('dfdf' , 'dfdfgffffffffffffff' , 't')
print(f'Самая длинная строка {max}')


# Normal, задача 1. Не в файле есть всё, тут показываем только бедных
def  proverka(zp,name):
    if zp <= 500000:
        print(f'{name} - {int(zp)}')


def nalog(stroka):
    a,b,c = stroka.split()
    c = int(c) * 0.87
    proverka(c,a)

names = ['ivan' , 'olga' , 'anna', 'semen']
salary = [200,500000000,300,600000]
spisok = dict(zip(names, salary))
print(spisok)
with open('salary.txt', 'w') as file:
    for i in range(len(names)):
        file.write(f'{names[i].upper()} - {salary[i]} \n')

with open('salary.txt', 'r') as file:
    for line in file:
        nalog(line)
#

# Normal, задача 1. В файле есть всё, тут показываем только бедных(учитывая вычет НДС)
def proverka(zp,name):
    if zp <= 500000:
        print(f'{name} - {int(zp)}')


def nalog(stroka):
    a,b,c = stroka.split()
    c = int(c) * 0.87
    proverka(c,a)

names = ['ivan' , 'olga' , 'anna', 'semen']
salary = [200,500000000,300,600000]
spisok = dict(zip(names, salary))
print(spisok)
with open('salary.txt', 'w') as file:
    for i in range(len(names)):
        file.write(f'{names[i].upper()} - {salary[i]} \n')

with open('salary.txt', 'r') as file:
    for line in file:
        nalog(line)


Normal, задача 1. Не пишем бедных в файл

def proverka(stroka):
    a,b,c = stroka.split()
    c = int(c)
    if c <= 500000:
        return True
names = ['ivan' , 'olga' , 'anna', 'semen']
salary = [200,500000000,300,600000]
spisok = dict(zip(names, salary))
print(spisok)
n = 0
with open('salary.txt', 'w') as file:
    for i in range(len(names)-1):
        test_str = f'{names[i].upper()} - {salary[i]} \n'
        if proverka(test_str) == True:
            file.write(test_str)
            n += 1
print(f'В компании {n} людей, зарабатывающих меньше 500000. Их имена и зп записаны в файл salary.txt')


# Hard
import random

def create_file(igrok, file_name):
    with open(file_name, 'w') as file:
        for key, val in igrok.items():
            file.write(f'{key} {val}\n')

def read_file(file_name):
    with open(file_name, 'r') as file:
        new_dict = {}
        for i in file.readlines():
            key, val = i.strip().split(' ')
            new_dict[key] = val
        return new_dict

def attack(player_1, enemy_1, kto_atakuet):
    enemy_1["health"] = int(enemy_1["health"]) - int(random.randint(1,max_dam) / armor)
    # enemy_1["health"] = int(enemy_1["health"]) - int(dam_arm(player_1['damage'] , enemy_1['arm']))
    #В текущем варианте урон игроков всегда уникальный. Если надо чтоб били уроном из словаря, то
    #надо  раскомментить строку выше и функцию dam_arm.

# def dam_arm(dama, arm):
#     real_dam = int(dama) / float(arm)
#     return real_dam


def game(pla, ene, name_1, name_2):
    while pla['health'] > 0 and ene['health'] > 0:
        attack(pla, ene, name_1)
        attack(ene, pla, name_2)
        print(f"У игрока {name_1} осталось {pla['health']} жизней")
        print(f"У игрока {name_2} осталось {ene['health']} жизней")
    else:
        if pla['health'] > ene['health'] and pla['health'] > 0:
            print(f'Игрок {name_1} выиграл!')
        elif pla['health'] < ene['health']  and ene['health'] >0:
            print(f'Игрок {name_2} выиграл!')
        else:
            print('Оба сдохли!')

def str_to_int(slovar):
    slovar['health'] = int(slovar['health'])
    slovar['damage'] = int(slovar['damage'])
    slovar['arm'] = float(slovar['arm'])


name_1 = input('введите имя игрока ')
name_2 =input('введите имя мишени ')
max_dam =int(input('Введите максимальный урон'))
health_1 =int(input('введите ХП'))
armor = float(input('Введите коэфф. брони'))
a = 'player.txt'
b = 'enemy.txt'
player = {'name' : name_1 , 'health' : health_1 , 'damage' : random.randint(1,max_dam) , 'arm' : armor}
enemy = {'name' : name_2 , 'health' : health_1, 'damage' : random.randint(1,max_dam) , 'arm' : armor}

create_file(player, a)
create_file(enemy, b)

print(player)
print(enemy)
# attack(player,enemy, name_1)
# print(f"У игрока {enemy['name']} осталось {int(enemy['health'])} жизней из {health_1}. Нанесено {player['damage']}"
#       f" урона, через броню прошло {int(dam_arm(player['damage'] , enemy['arm']))}")


# game(player, enemy, name_1, name_2)

player_from_file = read_file(a)
enemy_from_file = read_file((b))

str_to_int((player_from_file))
str_to_int(enemy_from_file)

game(player_from_file, enemy_from_file, name_1, name_2)
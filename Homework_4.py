# coding: 'UTF-8'

# Easy, задача 1
# spisok = [1, 4, 7, 2, 9, 1]
# nov_spisok = [i**2 for i in spisok]
# print(nov_spisok)

# Easy, задача 2
# sp_1 = ['банан', 'яблоко', 'ананас', 'арбуз']
# sp_2 = ['яблоко', 'банан', 'дыня', 'абрикос']
# sp_3 = [i for i in sp_1 if i in sp_2]
# print(sp_3)

# Easy, задача 3
# spisok = [1, 4, 3, 4, 7, 2, 9, 1]
# nov_spisok = [i for i in spisok if i % 3 == 0 and i > 0 and i % 4 != 0]
# print(nov_spisok)

# Normal, задача 1
# import re
# pattern = '^[A-Z]{1}[a-z]+$'
# pattern_2 = '^[a-z]+_*[0-9]*@[a-z]+[0-9]*\.(ru|org|com)$'
# name = 'Dima'
# fam = 'Smolkin'
# email = 'gazprom05@mail.ru'
# if re.match(pattern, name) is None or re.match(pattern, fam) is None:
#     print(f'{name} {fam} Имя или фамилия введены неверно')
# else:
#     print(f'{name} {fam} Имя и фамилия введены верно')
# if re.search(pattern_2, email) is None:
#     print(f'{email} введён неверно')
# else:
#     print(f'{email} введён верно')
# не смог решить через except SyntaxError :(

# Normal, задача 2
# import re
# some_str = 'Мороз и солнце; день чудесный!' \
#            'Еще ты дремлешь, друг прелестный —' \
#            'Пора, красавица, проснись:' \
#            'Открой сомк.....нуты негой взоры' \
#            'Навстречу северной Авроры'
# pattern = '\.{2,}'
# if re.search(pattern, some_str) is None:
#     print('В тексте нет двух точек подряд')
# else:
#     print('Есть две или более точки подряд')


# Hard
person1 = {'card': 4276123465440000, 'pin': 9090, 'money': 100.90}
person2 = {'card': 4276123465440001, 'pin': 9091, 'money': 200.90}
person3 = {'card': 4276123465440002, 'pin': 9092, 'money': 300.90}

bank = [person1, person2, person3]


def get_person_by_card(card_number):
    for person in bank:
        if person['card'] == card_number:
            return person


def is_pin_valid(person, pin_code):
    if person['pin'] == pin_code:
        return True
    return False


def check_account(person):
    return round(person['money'], 2)


def withdraw_money(person, money):
    if person['money'] - money > 0:
        person['money'] -= money
        return 'Вы сняли {} рублей.'.format(money)
    else:
        return 'На вашем счету недостаточно средств!'


def process_user_choice(choice, person):
    if choice == 1:
        print(check_account(person))
    elif choice == 2:
        count = float(input('Сумма к снятию:'))
        print(withdraw_money(person, count))


def start():
    try:
        card_number, pin_code = input('Введите номер карты и пин код через пробел:').split()
        card_number = int(card_number)
        pin_code = int(pin_code)
    except ValueError:
        print('Номер или пин введены неверно')
    else:
        person = get_person_by_card(card_number)
        if person and is_pin_valid(person, pin_code):
            while True:
                try:
                    choice = int(input('Выберите пункт:\n'
                                   '1. Проверить баланс\n'
                                   '2. Снять деньги\n'
                                   '3. Выход\n'
                                   '---------------------\n'
                                   'Ваш выбор:'))
                    if choice == 3:
                        break
                    process_user_choice(choice, person)
                except ValueError:
                    print('Введите число от 1 до 3')
        else:
            print('Номер карты или пин код введены не верно!')


start()




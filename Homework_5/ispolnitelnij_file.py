# coding: UTF-8

from libs import homework

# print(libs.homework.make_new_dirs())  # Easy 1
# print(libs.homework.delete_dirs())    # Easy 1
# print(libs.homework.spisok_papok())   # Easy 2
#
# print(homework.copir())          # Easy 3. Данное решение работает только
# если исполнитель и скрипт лежат в 1 папке. Универсального красивого решения пока не придумал.


# Normal

# os.listdir()
# libs.homework.pri()
#
#
# while True:
#     try:
#         vibor = int(input('выберите действие:\n'
#                       '1. Перейти в папку\n'
#                       '2. Посмотреть содержимое текущей папки\n'
#                       '3. удалить папку\n'
#                       '4. создать папку\n'
#                           '5. выход'))
#         if vibor == 1:
#             name = input('Введите имя папки, куда надо перейти\n')
#             libs.homework.change_dir(name)
#         if vibor == 2:
#             libs.homework.list_dir()
#         if vibor == 3:
#             name = input('Введите имя папки для удаления\n')
#             libs.homework.delete_dir(name)
#         if vibor ==4:
#             name = input('Введите имя папки для создания\n')
#             libs.homework.create_dir(name)
#         if vibor == 5:
#             print('Вы вышли из программы')
#             break
#     except ValueError:
#         print('Введите правильную цифру')
#         continue


import with_args
print(with_args(a,s))
# coding: UTF-8

# Easy, задача 1
import os
import shutil

def make_new_dirs():
    try:
        for i in range(9):
            os.mkdir(f'dir{i+1}', 0o777)
        return 'я создал папки'
    except FileExistsError:
        print('Такие папки уже есть')
def delete_dirs():
    try:
        for i in range(9):
            os.rmdir(f'dir{i+1}')
        return 'я удалил папки'
    except FileNotFoundError:
        return 'Таких папок нет'
# Easy, задача 2

def spisok_papok():
    print(os.listdir())
    return 'я вывел список директорий'

# Easy, задача 3
#
def copir():
    a,b =__name__.split('.')
    shutil.copyfile(os.path.abspath(f'{b}.py'), os.path.abspath(f'{b}_1.py'))
    print(os.listdir())
    return 'я скопировл исходный файл'


# Normal

# def pri():
#     print('hello world')
#
# def change_dir(name):
#     try:
#         os.chdir(name)
#         print('я перешел в папку' , name)
#         print()
#     except FileNotFoundError:
#         print('нет такой папки\n')
#
# def list_dir():
#     print('Я вывел список файлов:')
#     print(os.listdir())
#     print()
#
# def delete_dir(name):
#     try:
#         os.rmdir(name)
#         print((f'Я удалил папку {name}\n'))
#     except FileNotFoundError:
#         print('нет такой папки\n')
#
# def create_dir(name):
#     try:
#         os.mkdir(name, mode=0o777)
#         print((f'Я создал папку {name}\n'))
#     except FileExistsError:
#         print('такая папка уже существует')


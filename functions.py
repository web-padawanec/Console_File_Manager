import os
import shutil
import os.path
import platform


def create_new_dir():
    name_folder = input(f'\n1. Введите имя новой папки ')
    if not os.path.exists(name_folder):
        os.mkdir(name_folder)
    else:
        print('Такая папка уже есть')


def remove_dir():
    name_folder = input(f'\n2. Введите имя удаляемой папки ')
    if os.path.exists(name_folder):
        os.rmdir(name_folder)
    else:
        print('Такой папки нет')


def copy_dir():
    old_folder = input(f'\n3. Введите имя копируемой папки: ')
    new_folder = input('Введите имя новой папки: ')
    shutil.copytree(old_folder, new_folder)


def list_dir():
    print(f'\n5. Папки в директории {os.getcwd()}: ')
    for something in os.listdir():
        if os.path.isdir(something):
            print(something)


def list_files():
    print(f'\n6. Файлы в директории {os.getcwd()}: ')
    for something in os.listdir():
        if os.path.isfile(something):
            print(something)


def chehge_dir():
    print('\nВы находитесь здесь:')
    print(f'{os.getcwd()}')
    new_path = input('\nВведите путь куда хотите перейти ')
    if os.path.exists(new_path):
        os.chdir(new_path)
        print('Теперь Вы находитесь:  ')
        print(os.getcwd())
    else:
        print('Нет такой папки')

import os.path
import platform
from victory import victorin
from bank_score import bank_score
from functions import create_new_dir, remove_dir, copy_dir, list_dir, list_files, chehge_dir

if __name__ == '__main__':
    while True:
        print('\nВведите номер пункта меню: ')
        print('1 - создать папку')
        print('2 - удалить (файл/папку)')
        print('3 - копировать (файл/папку)')
        print('4 - просмотр содержимого рабочей директории')
        print('5 - посмотреть только папки')
        print('6 - посмотреть только файлы')
        print('7 - просмотр информации об операционной системе')
        print('8 - создатель программы')
        print('9 - играть в викторину')
        print('10 - мой банковский счет')
        print('11 - смена рабочей директории')
        print('12 - выход.')
        os.sync()

        menu_item = input('Выберите пункт меню ')
        if menu_item == '1':
            create_new_dir()
        elif menu_item == '2':
            remove_dir()
        elif menu_item == '3':
            copy_dir()
        elif menu_item == '4':
            print(f'\n4. содержимое рабочей директории:')
            print(*os.listdir(), sep='; ')
        elif menu_item == '5':
            list_dir()
        elif menu_item == '6':
            list_files()
        elif menu_item == '7':
            print(f'\n7. Ваша операционная система: {os.name} {platform.system()} {platform.release()}')
        elif menu_item == '8':
            print(f'\n8. Сию недостойную программу накорябал я, Артур Рудин. ')
        elif menu_item == '9':
            print(f'\n9. ВИКТОРИНА! ')
            victorin()
        elif menu_item == '10':
            print(f'\n10. Банковский счет \n')
            bank_score()
        elif menu_item == '11':
            print(f'\n11. Смена рабочей директории ')
            chehge_dir()
        elif menu_item == '12':
            break
        else:
            print('Неверный пункт меню')

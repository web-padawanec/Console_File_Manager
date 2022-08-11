import os
import shutil
import os.path
import platform

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
            name_folder = input(f'\n1. Введите имя новой папки ')
            if not os.path.exists(name_folder):
                os.mkdir(name_folder)
            else:
                print('Такая папка уже есть')
        elif menu_item == '2':
            name_folder = input(f'\n2. Введите имя удаляемой папки ')
            if os.path.exists(name_folder):
                os.rmdir(name_folder)
            else:
                print('Такой папки нет')
        elif menu_item == '3':
            old_folder = input(f'\n3. Введите имя копируемой папки: ')
            new_folder = input('Введите имя новой папки: ')
            shutil.copytree(old_folder, new_folder)
        elif menu_item == '4':
            print(f'\n4. содержимое рабочей директории:')
            print(*os.listdir(), sep='; ')
        elif menu_item == '5':
            print(f'\n5. Папки в директории {os.getcwd()}: ')
            for something in os.listdir():
                if os.path.isdir(something):
                    print(something)
        elif menu_item == '6':
            print(f'\n6. Файлы в директории {os.getcwd()}: ')
            for something in os.listdir():
                if os.path.isfile(something):
                    print(something)
        elif menu_item == '7':
            print(f'\n7. Ваша операционная система: {os.name} {platform.system()} {platform.release()}')
        elif menu_item == '8':
            print(f'\n8. Сию недостойную программу накорябал я, Артур Рудин. ')
        elif menu_item == '9':
            print(f'\n9. ВИКТОРИНА! ')
        elif menu_item == '10':
            print(f'\n10. Банковский счет ')
        elif menu_item == '11':
            print(f'\n11. Смена рабочей директории ')
            print('\nВы находитесь здесь:')
            print(f'{os.getcwd()}')
            new_path = input('\nВведите путь куда хотите перейти ')
            if os.path.exists(new_path):
                os.chdir(new_path)
                print('Теперь Вы находитесь:  ')
                print(os.getcwd())
            else:
                print('Нет такой папки')
        elif menu_item == '12':
            break
        else:
            print('Неверный пункт меню')

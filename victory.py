import random


def victorin():
    days = {
        '01': 'первого', '02': 'второго', '03': 'третьего', '04': 'четвёртого', '05': 'пятого',
        '06': 'шестого', '07': 'седьмого', '08': 'восьмого', '09': 'девятого', '10': 'десятого',
        '11': 'одиннадцатого', '12': 'двенадцатого', '13': 'тринадцатого', '14': 'четырнадцатого',
        '15': 'пятнадцатого', '16': 'шестнадцатого', '17': 'семнадцатого', '18': 'восемнадцатого',
        '19': 'девятнадцатого', '20': 'двадцатого', '21': 'двадцать первого', '22': 'двадцать второго',
        '23': 'двадцать третьего', '24': 'двадцать четвёртого', '25': 'двадцать пятого',
        '26': 'двадцать шестого', '27': 'двадцать седьмого', '28': 'двадцать восьмого',
        '29': 'двадцать девятого', '30': 'тридцатого', '31': 'тридцать первого',
    }

    months = {
        '01': 'января', '02': 'февраля', '03': 'марта', '04': 'апреля', '05': 'мая', '06': 'июня',
        '07': 'июля', '08': 'августа', '09': 'сентября', '10': 'октября', '11': 'ноября', '12': 'декабря'
    }

    famous_people = {
        'И.Ньютон': '25.12.1642',
        'М.В.Ломоносов': '08.11.1711',
        'Л.Н.Толстой': '09.09.1828',
        'Д.И.Менделеев': '27.01.1834',
        'А.Эйнштейн': '14.03.1879',
        'И.В.Сталин': '09.12.1879',
        'С.П.Королёв': '12.01.1907',
        'Ю.А.Гагарин': '09.03.1934',
        'В.С.Высоцкий': '25.01.1938',
        'В.В.Путин': '07.10.1952'
    }

    cycle = "Y"
    while cycle.upper() == "Д" or cycle.upper() == "Y":
        answer_correct = 0
        answer_wrong = 0
        random_list = []

        for key in famous_people:
            random_list.append(key)
        list_victory = random.sample(random_list, 5)

        for i in list_victory:
            birthday = input(f"Когда родился {i} \nвведите дату в формате 'dd.mm.yyyy' ")
            if birthday == famous_people[i]:
                print("Правильно!")
                answer_correct += 1
            else:
                dey, month, year = famous_people[i].split('.')
                print(dey, month, year)
                print(f'Неверно \n {i} родился {days[dey]} {months[month]} {year}')
                answer_wrong += 1

        print(f"\nПравильных ответов: {answer_correct}")
        print(f"Неправильных ответов: {answer_wrong}")
        print("процент правильных ответов: ", answer_correct * 100 / 5,'%')
        print("процент ошибок: ", answer_wrong * 100 / 5,'%')
        cycle = input("\nХотите попробовать ещё раз?, Д/Н или Y/N ")

    print("bye!")
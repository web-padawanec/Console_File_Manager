def bank_score():
    score = 0
    purchases_history = []  # Список покупок

    def buy(s):
        b = int(input('Введите сумму покупки: '))
        if b > s:
            print('Для этой покупки у Вас недостаточно средств на счёте')
        else:
            s -= b
            i = input('Введите название покупки: ')
            purchases_history.append((i, b))
        return s

    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')
        print(f'Выш счёт {score}')

        choice = input('Выберите пункт меню ')
        if choice == '1':
            x = int(input('Введите сумму, которую хотите внести на счёт: '))
            score += x
        elif choice == '2':
            score = buy(score)
        elif choice == '3':
            print('Ваша история покупок:')
            print(purchases_history)
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')

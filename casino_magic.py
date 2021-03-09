import random


def magic(all_points):
    rules()
    random_number = random.randint(1, 10)
    print("Угадайте число от 1 до 10")
    while True:
        counter = 0
        try:
            number = int(input("Ваше число: "))
            counter += 1
        except ValueError:
            print('Должно быть число')
            continue
        if number > random_number:
            print(f'магическое число меньше {number}')
        elif number < random_number:
            print(f'магическое число больше {number}')
        else:
            print(f'\nВы угадали, число {number}')
            print("Попыток:", counter)
#            random_number = random.randint(1, 10)
            points_1 = 0
            if counter == 1:
                print(f"Вам начислено 50 очкев")
                points_1 = 50
            elif counter == 2:
                print("Вам начислено 25 очков")
                points_1 = 25
            elif counter == 3:
                print("Вам начислено 10 очков")
                points_1 = 10
            elif counter == 4:
                print("Вам начислено 5 очков")
                points_1 = 5
            else:
                print("Вам начислено 0 очков")

            if all_points == 0:
                all_points = points_1
            else:
                all_points += points_1
            print(f'Теперь у вас {all_points} очков')
            break

        if counter == 5:
            print(f'\nБыло загадано число {random_number}')
            print('Все попытки кончились')
            break
    next_action = input('\nИграем ещё раз? (y/n): \n')
    if next_action == "y":
        magic(all_points)
    else:
        return all_points


def rules():
    if input('Введите "r" для прочтения правил игры или нажмите Enter для продолжения: \n') == 'r':
        print('''
                Правила игры "Magic":
                Компьютер загадывает число, а вы должны угадать его за наименьшее число попыток.
                Начисление очков за количество попыток:
                1я попытка - 50 очков
                2я попытка - 25 очков
                3я попытка - 10 очков
                4я попытка - 5 очков
                5я попытка - 0 очков
           \n''')
    else:
        return 0

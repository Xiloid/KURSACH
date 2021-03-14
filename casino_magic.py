import json
import random


def magic(player_name):
    random_number = random.randint(1, 10)
    counter = 1
    magic_points = 0
    def_data = {'overall_stat': 20, 'm_games': 0, 'm_win': 0, 'm_average': 0, 'm_record': 0,
                'b_games': 0, 'b_win': 0, 'b_average': 0}
    with open('data.json') as f:
        all_file_data = json.load(f)
        player_data = all_file_data.get(player_name, def_data)  # если нет игрока, пишем дефолт значение

    print("Компьютер загадал число. Отгадайте его. У вас 5 попыток")
    while counter <= 5:
        try:
            number = int(input(str(counter) + '-я попытка: '))
        except ValueError:
            print('Должно быть целое число!')
            continue
        if number > random_number:
            print('Много')
        elif number < random_number:
            print('Мало')
        else:
            print(f'Вы угадали с {counter}-й попытки')
            break
        counter += 1
    else:
        print(f'Вы не угадали с 5 попыток и оштрафованы на 5 очков. Было загадано число {random_number}')
        player_data['overall_stat'] -= 5  # штраф 5 очков
    if counter == 1:
        magic_points = 20
        print(f'Вам начислено {magic_points} очков')
    elif counter == 2:
        magic_points = 15
        print(f'Вам начислено {magic_points} очков')
    elif counter == 3:
        magic_points = 10
        print(f'Вам начислено {magic_points} очков')
    elif counter == 4:
        magic_points = 5
        print(f'Вам начислено {magic_points} очков')
    elif player_data['overall_stat'] <= 0:
        print('Ой, Вы банкрот! (персональных очков ноль или минус), игра дает Вам в кредит 20 очков :)')
        player_data['overall_stat'] += 25
    player_data['overall_stat'] += magic_points  # плюсуем заработанные очки

    if not player_data['m_record'] or player_data['m_record'] > counter:
        player_data['m_record'] = counter
    if counter < 5:
        player_data['m_win'] += 1   # если угадано до 5 попыток, плюсуем счетчик "выигрышей"
    games = player_data['m_games']  # переменная кол-ва игр
    avg = player_data['m_average']  # переменная для высчета среднего коэффициента
    player_data['m_games'] += 1  # плюсуем счетчик игр всего
    player_data['m_average'] = round((games * avg + counter) / (games + 1), 2)  # средний коэффициент, округл. до 2 зн.

    with open('data.json', 'w') as f:
        all_file_data[player_name] = player_data
        f.seek(0)
        f.write(json.dumps(all_file_data, indent=4))
        f.close()

    next_action = input('\nИграем ещё раз? (y/n): \n')
    if next_action == "y":
        magic(player_name)
    else:
        return 0

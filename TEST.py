import json
import random


def main():
    all_points = 0
    magic(all_points)


def magic(all_points):
    player_name = (input('Введите имя игрока: '))
    def_data = {'overall_stat': 0, 'm_games': 0, 'm_win': 0, 'm_average': 0, 'm_record': 0}
    with open('data.json') as f:
        all_file_data = json.load(f)
        player_data = all_file_data.get(player_name, def_data)

    random_number = random.randint(1, 10)
    counter = 0
    magic_points = 0
    while True:
        try:
            number = int(input('Угадайте число от 1 до 10. Ваше число: '))
            counter += 1
        except ValueError:
            print('Должно быть целое число!')
            continue
        if number > random_number:
            print(f'магическое число меньше {number}')
        elif number < random_number:
            print(f'магическое число больше {number}')
        else:
            print(f'\nВы угадали, число {number}')
            print("Попыток:", counter)

            if counter == 1:
                magic_points = 50
                print(f'Вам начислено {magic_points} очков')
            elif counter == 2:
                magic_points = 25
                print(f'Вам начислено {magic_points} очков')
            elif counter == 3:
                magic_points = 10
                print(f'Вам начислено {magic_points} очков')
            elif counter == 4:
                magic_points = 5
                print(f'Вам начислено {magic_points} очков')
            else:
                print('Вам не начислено очков, т.к. магическое число угадано с последней попытки')

            if not player_data['m_record'] or player_data['m_record'] > counter:
                player_data['m_record'] = counter
            if counter < 5:
                player_data['m_win'] += 1
            games = player_data['m_games']
            avg = player_data['m_average']
            player_data['m_games'] += 1
            player_data['m_average'] = (games * avg + counter) / (games + 1)

            if all_points == 0:
                all_points = magic_points

            else:
                all_points += magic_points
            print(f'Теперь у вас {all_points} очков')
            break

        if counter > 4:
            player_data['m_games'] += 1
            print(f'\nК сожалению попытки кончились. Было загадано число {random_number}')
            break

    with open('data.json', 'r+') as f:
        all_file_data = json.load(f)
        all_file_data[player_name] = player_data
        all_file_data = json.dumps(all_file_data, indent=4)
        f.seek(0)
        f.write(all_file_data)

    next_action = input('\nИграем ещё раз? (y/n): \n')
    if next_action == "y":
        magic(all_points)
    else:
        print(all_points)


if __name__ == "__main__":
    main()

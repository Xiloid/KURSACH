import json
import random

player_name = (input('Введите имя игрока: '))
def_data = {'overall_stat': 0, 'm_all': 0, 'm_win': 0, 'm_koef': 0, 'm_rec': 0,
            'b_all': 0, 'b_win': 0, 'b_koef': 0}
with open('data.json') as f:
    players_data = json.load(f)
    player_data = players_data.get(player_name, def_data)

def magic(all_points):
    random_number = random.randint(1, 10)
    print("Угадайте число от 1 до 10")
    counter = 0
    while True:
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

    with open('data.json', 'r+') as f:
        players_data = json.load(f)
        players_data[player_name] = player_data
        players_data = json.dumps(players_data, indent=4)
        f.seek(0)
        f.write(players_data)

    next_action = input('\nИграем ещё раз? (y/n): \n')
    if next_action == "y":
        magic(all_points)
    else:
        print(all_points)
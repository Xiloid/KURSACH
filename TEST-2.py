import json
import random


def main():
    stat()
    # magic()


def magic():
    player_name = (input('Введите имя игрока: '))
    def_data = {'overall_stat': 0, 'm_games': 0, 'm_win': 0, 'm_average': 0, 'm_record': 0}
    with open('data.json') as f:
        all_file_data = json.load(f)
        player_data = all_file_data.get(player_name, def_data)

    random_number = random.randint(1, 10)
    counter = 1
    magic_points = 0
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
        print(f'Вы исчерпали 5 попыток. Было загадано число {random_number}')
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
    else:
        print('Вам не начислено очков, т.к. магическое число угадано с последней попытки')
    print(magic_points)

    if not player_data['m_record'] or player_data['m_record'] > counter:
        player_data['m_record'] = counter
    if counter < 5:
        player_data['m_win'] += 1
    games = player_data['m_games']
    avg = player_data['m_average']
    player_data['m_games'] += 1
    player_data['m_average'] = (games * avg + counter) / (games + 1)

    with open('data.json', 'r+') as f:
        all_file_data = json.load(f)
        all_file_data[player_name] = player_data
        all_file_data = json.dumps(all_file_data, indent=4)
        f.seek(0)
        f.write(all_file_data)

    next_action = input('\nИграем ещё раз? (y/n): \n')
    if next_action == "y":
        magic()
    else:
        print('EXIT')


def stat():
    player_name = (input('Введите имя игрока: '))
    with open('data.json') as f:
        all_file_data = json.load(f)
        q = all_file_data.get(player_name)
        if q:
            print(f'''
            Имя игрока: {player_name}
            Количество очков: {q["overall_stat"]}
            
            ----- MAGIC -----
            Количество очков: {q["overall_stat"]}        
            Всего игр сыграно: {q["m_games"]}
            Выиграно: {q["m_win"]}
            Коэффициент выигрышей: {q["m_average"]}
            Рекордное количество попыток: {q["m_record"]}
            
            ----- BLACKJACK -----
            Всего игр сыграно: 
            Выиграно: 
            Коэффициент выигрышей: 
            ''')
        else:
            print('Игрок с данным именем не найден!')
            stat()


def del_player():
    pass


if __name__ == "__main__":
    main()

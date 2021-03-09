import json
import random


def main():
    # add_player()
    del_player()
    # stat()
    # magic()


def magic():
    random_number = random.randint(1, 10)
    counter = 1
    magic_points = 0
    player_name = (input('Введите имя игрока: '))
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
        print('Вы банкрот (персональных очков ноль или минус), игра начисляет Вам первоначальные 20 очков.')
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

    next_action = input('\nИграем ещё раз? (y/n): \n')
    if next_action == "y":
        magic()
    else:
        print('EXIT')


def stat():
    player_name = (input('Введите имя игрока: '))
    with open('data.json') as f:
        all_file_data = json.load(f)
        player_data = all_file_data.get(player_name)
        if player_data:
            print(f'''
            Имя игрока: {player_name}
            Общее количество очков: {player_data["overall_stat"]}
            
            ----- MAGIC -----
            Количество очков: {player_data["overall_stat"]}        
            Всего игр сыграно: {player_data["m_games"]}
            Выиграно: {player_data["m_win"]}
            Коэффициент выигрышей: {player_data["m_average"]}
            Рекордное количество попыток: {player_data["m_record"]}
            
            ----- BLACKJACK -----
            Всего игр сыграно: {player_data["b_games"]}
            Выиграно: {player_data["b_win"]}
            Коэффициент выигрышей: {player_data["b_average"]}
            ''')
        else:
            print('Игрок с данным именем не найден!')
            stat()


def del_player():
    with open('data.json', 'r') as f:       # читаем файл и закрываем, что-бы не было дозаписи
        all_file_data = json.load(f)        # переменная в которой весь файл
        f.close()
    with open('data.json', 'w') as f:       # открываем снова пустой файл и после операции по удалению...
        while True:                         # ...записываем значение переменной all_data_file в json
            player_name = (input('Введите имя игрока для удаления: '))
            if all_file_data.get(player_name):
                if input(f'''
                Вы точно хотите удалить игрока "{player_name}" и всю его статистику??
                Эти действия необратимы!!
                Введите "yes" для продолжения или любую клавишу для отмены\n''') == 'yes':
                    all_file_data.pop(player_name)
                    f.seek(0)
                    f.write(json.dumps(all_file_data, indent=4))
                    f.close()
                    print(f'\nИгрок "{player_name}" удалён из базы.')
                    break
                else:
                    f.write(json.dumps(all_file_data, indent=4))
                    f.close()
                    exit('выход....')
                    # del_player()  # тут переход обратно в меню
            else:
                print(f'Игрока "{player_name}" нет в базе, попробуйте снова!')
                continue
    return 0


def add_player():
    def_data = {'overall_stat': 20, 'm_games': 0, 'm_win': 0, 'm_average': 0, 'm_record': 0,
                'b_games': 0, 'b_win': 0, 'b_average': 0}
    with open('data.json') as f:
        all_file_data = json.load(f)
        f.close()
    with open('data.json', 'w') as f:
        while True:
            player_name = (input('Введите имя нового игрока: '))
            if all_file_data.get(player_name):
                print(f'Игрок "{player_name}" уже есть в базе, введите другое имя!')
                continue
            else:
                player_data = all_file_data.get(player_name, def_data)
                all_file_data[player_name] = player_data
                f.seek(0)
                f.write(json.dumps(all_file_data, indent=4))
                f.close()
                print(f'Игрок "{player_name}" записан!')
                break
    return 0


if __name__ == "__main__":
    main()

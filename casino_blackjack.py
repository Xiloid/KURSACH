import random
import json


def main():
    player_name = (input('Введите имя игрока: '))
    blackjack(player_name)


def blackjack(player_name):
    def_data = {'overall_stat': 20, 'm_games': 0, 'm_win': 0, 'm_average': 0, 'm_record': 0,
                'b_games': 0, 'b_win': 0, 'b_average': 0}
    with open('data.json') as f:
        all_file_data = json.load(f)
        player_data = all_file_data.get(player_name, def_data)  # если нет игрока, пишем дефолт значение
    player_points = int(player_data['overall_stat'])
    games = player_data['b_games']  # переменная кол-ва игр
    avg = player_data['b_average']  # переменная для высчета среднего коэффициента
    while True:
        counter = 0
        start = input('\nНажмите "Enter" что бы начать игру или введите "q" для выхода \n')
        if start != 'q':
            bet = int(input('Сделайте Вашу ставку: '))
            if player_points < bet:  # проверка, можно ли игроку столько ставить или нет очков
                print(f'Ваша ставка "{bet}" больше, чем общее количество Ваших очков: {player_points}')
                continue
            player_points -= bet  # забираем очки в размере ставки сразу
            player_data['b_games'] += 1
            # games += 1  # инкремент количества игр
            deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
            count = 0
            random.shuffle(deck)

            while True:
                # counter += 1
                choice = input('\nЕщё карту: "y" Если хватит: "n" ')
                if choice == 'y':
                    counter += 1
                    current = deck.pop()
                    if current == 11 and count > 10:
                        current = 1
                        print(f'\nВыпал "Туз", и т.к. на руках {count} очков, трактуем его как 1')
                    count += current
                    print(f'\nВам попалась карта достоинством {current}, теперь у вас {count} очков')
                    if count > 21:
                        print(f'\nК сожалению у Вас перебор! Ваша ставка в {bet} очков снимается в пользу казино!')
                        # Ничего не делаем, т.к. очки уже забрали в начале (ставка снимается в пользу казино)
                        break
                    elif count == 21:
                        print(f'\nПоздравляем, Вы выиграли! Ваша ставка "{bet}" возвращена в удвоенном размере!')
                        player_points += bet * 2  # игроку возвращается удвоенная ставка
                        player_data['b_win'] += 1
                        break
                else:
                    print(f'\nПас! На руках {count} очков. Ваша ставка "{bet}" возвращена')
                    player_points += bet  # возврат очков обратно
                    break
        else:
            break
        player_data['b_average'] = round((games * avg + counter) / (games + 1), 2)  # средний коэффициент
    # тут возврат в меню
    player_data['overall_stat'] = player_points
    with open('data.json', 'w') as f:
        all_file_data[player_name] = player_data
        f.seek(0)
        f.write(json.dumps(all_file_data, indent=4))
        f.close()
    print('\nПока! Пока!')


if __name__ == "__main__":
    main()

import random
import json
from colorama import Fore, Style
from colorama import init
init()


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
        start = input(Fore.MAGENTA + '\nНажмите "Enter" что бы начать игру или введите "q" для '
                                     'выхода \n' + Style.RESET_ALL)
        if start != 'q':
            if player_points <= 0:
                print(Fore.RED + 'Ой, Вы банкрот (персональных очков ноль или минус), игра дает Вам в кредит 20 '
                                 'очков :)' + Style.RESET_ALL)
                player_points += 20
                continue
            bet = int(input(Fore.BLUE + 'Сделайте Вашу ставку: ' + Style.RESET_ALL))
            if player_points < bet:  # проверка, можно ли игроку столько ставить или нет очков
                print(Fore.RED + f'Ваша ставка "{bet}" больше, чем общее количество Ваших очков: '
                                 f'{player_points}' + Style.RESET_ALL)
                continue
            player_points -= bet  # забираем очки в размере ставки сразу
            player_data['b_games'] += 1
            deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
            count = 0
            random.shuffle(deck)

            while True:
                choice = input(Fore.GREEN + '\nЕщё карту: "y" Если хватит: "n" ' + Style.RESET_ALL)
                if choice == 'y':
                    counter += 1
                    current = deck.pop()
                    if current == 11 and count > 10:
                        current = 1
                        print(Fore.CYAN + f'\nВыпал "Туз", и т.к. на руках {count} очков, трактуем его '
                                          f'как 1' + Style.RESET_ALL)
                    count += current
                    print(Fore.LIGHTGREEN_EX + f'\nВам попалась карта достоинством {current}, теперь у вас {count} '
                                               f'очков' + Style.RESET_ALL)
                    if count > 21:
                        print(Fore.RED + f'\nК сожалению у Вас перебор! Ваша ставка в {bet} очков снимается в пользу '
                                         f'казино!' + Style.RESET_ALL)
                        break
                    elif count == 21:
                        print(Fore.CYAN + f'\nПоздравляем, Вы выиграли! Ваша ставка "{bet}" возвращена в удвоенном '
                                          f'размере!' + Style.RESET_ALL)
                        player_points += bet * 2  # игроку возвращается удвоенная ставка
                        player_data['b_win'] += 1
                        break
                else:
                    print(Fore.CYAN + f'\nПас! На руках {count} очков. Ваша ставка "{bet}" '
                                      f'возвращена' + Style.RESET_ALL)
                    player_points += bet  # возврат очков обратно
                    break
        else:
            break
        player_data['b_average'] = round((games * avg + counter) / (games + 1), 2)  # средний коэффициент
    player_data['overall_stat'] = player_points
    with open('data.json', 'w') as f:
        all_file_data[player_name] = player_data
        f.seek(0)
        f.write(json.dumps(all_file_data, indent=4))
        f.close()
    print(Fore.BLUE + '\nПока! Пока!' + Style.RESET_ALL)
    return 0

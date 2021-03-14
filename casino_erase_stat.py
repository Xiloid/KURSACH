import json
from colorama import Fore, Style
from colorama import init
init()


def erase(player_name):
    def_data = {'overall_stat': 20, 'm_games': 0, 'm_win': 0, 'm_average': 0, 'm_record': 0,
                'b_games': 0, 'b_win': 0, 'b_average': 0}
    with open('data.json') as f:
        all_file_data = json.load(f)
        player_data = all_file_data.get(player_name)
        f.close()
        while True:
            if player_data:
                if input(Fore.RED + f'\nВы точно хотите удалить статистику игрока "{player_name}"??\
                            \nЭто действие необратимо!\
                            \nВведите "yes" для продолжения или ENTER для отмены\n' + Style.RESET_ALL) == 'yes':
                    with open('data.json', 'w') as f1:
                        all_file_data[player_name] = def_data
                        f1.seek(0)
                        f1.write(json.dumps(all_file_data, indent=4))
                        f1.close()
                        print(Fore.BLUE + f'\nСтатистика игрока {player_name} очищена' + Style.RESET_ALL)
                        break
                else:
                    with open('data.json', 'w') as f2:
                        f2.write(json.dumps(all_file_data, indent=4))
                        f2.close()
                        print(Fore.BLUE + '\nДействие по очистке статистики отменено.' + Style.RESET_ALL)
                        break
            else:
                print(Fore.RED + f'\nИгрока "{player_name}" нет в базе, попробуйте снова!\n'
                      f'Или начните любую игру, для добавления в базу как "{player_name}"' + Style.RESET_ALL)
                input(Fore.BLUE + 'Нажмите ENTER для продолжения...' + Style.RESET_ALL)
                break
    return 0


def stat(player_name):
    with open('data.json') as f:
        all_file_data = json.load(f)
        player_data = all_file_data.get(player_name)
        if player_data:
            print(Fore.LIGHTYELLOW_EX + f'''
            Имя игрока: {player_name}
            Общее количество очков: {player_data["overall_stat"]}

            ----- MAGIC -----
            Всего игр сыграно: {player_data["m_games"]}
            Выиграно: {player_data["m_win"]}
            Коэффициент выигрышей: {player_data["m_average"]}
            Рекордное количество попыток: {player_data["m_record"]}

            ----- BLACKJACK -----
            Всего игр сыграно: {player_data["b_games"]}
            Выиграно: {player_data["b_win"]}
            Коэффициент выигрышей: {player_data["b_average"]}
            ''' + Style.RESET_ALL)
            input(Fore.BLUE + 'Нажмите ENTER для продолжения...' + Style.RESET_ALL)
        else:
            print(Fore.RED + f'\nИгрока "{player_name}" нет в базе, попробуйте снова!\n'
                  f'Или начните любую игру, для добавления в базу как "{player_name}"' + Style.RESET_ALL)
            input(Fore.BLUE + 'Нажмите ENTER для продолжения...' + Style.RESET_ALL)
    return 0

import json


def erase(player_name):
    def_data = {'overall_stat': 20, 'm_games': 0, 'm_win': 0, 'm_average': 0, 'm_record': 0,
                'b_games': 0, 'b_win': 0, 'b_average': 0}
    with open('data.json') as f:
        all_file_data = json.load(f)
        player_data = all_file_data.get(player_name)
        f.close()
        while True:
            if player_data:
                if input(f'\nВы точно хотите удалить статистику игрока "{player_name}"??\
                            \nЭто действие необратимо!\
                            \nВведите "yes" для продолжения или ENTER для отмены\n') == 'yes':
                    with open('data.json', 'w') as f1:
                        all_file_data[player_name] = def_data
                        f1.seek(0)
                        f1.write(json.dumps(all_file_data, indent=4))
                        f1.close()
                        print(f'\nСтатистика игрока {player_name} очищена')
                        break
                else:
                    with open('data.json', 'w') as f2:
                        f2.write(json.dumps(all_file_data, indent=4))
                        f2.close()
                        print('\nДействие по очистке статистики отменено.')
                        break
            else:
                print(f'\nИгрока "{player_name}" нет в базе, попробуйте снова!\n'
                      f'Или начните любую игру, для добавления в базу как "{player_name}"')
                input('Нажмите ENTER для продолжения...')
                break
    return 0


def stat(player_name):
    with open('data.json') as f:
        all_file_data = json.load(f)
        player_data = all_file_data.get(player_name)
        if player_data:
            print(f'''
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
            ''')
            input('Нажмите ENTER для продолжения...')
        else:
            print(f'\nИгрока "{player_name}" нет в базе, попробуйте снова!\n'
                  f'Или начните любую игру, для добавления в базу как "{player_name}"')
            input('Нажмите ENTER для продолжения...')
    return 0

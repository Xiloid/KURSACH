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
                print(f'\nИгрока "{player_name}" нет в базе, попробуйте снова!')
                break
    return 0


# def del_player(player_name):
#     with open('data.json', 'r') as f:       # читаем файл и закрываем, что-бы не было дозаписи
#         all_file_data = json.load(f)        # переменная в которой весь файл
#         f.close()
#     with open('data.json', 'w') as f:       # открываем снова пустой файл и после операции по удалению...
#         while True:                         # ...записываем значение переменной all_data_file в json
#             if all_file_data.get(player_name):
#                 if input(f'''\n
#                 Вы точно хотите удалить игрока "{player_name}" и всю его статистику??
#                 Это действие необратимо!
#                 Введите "yes" для продолжения или любую клавишу для отмены\n''') == 'yes':
#                     all_file_data.pop(player_name)
#                     f.seek(0)
#                     f.write(json.dumps(all_file_data, indent=4))
#                     f.close()
#                     print(f'\nИгрок "{player_name}" удалён из базы.')
#                     break
#                 else:
#                     f.write(json.dumps(all_file_data, indent=4))
#                     f.close()
#                     print('\nДействие по удалению отменено.')
#                     break
#             else:
#                 print(f'\nИгрока "{player_name}" нет в базе, попробуйте снова!')
#                 continue
#     return 0


# def add_player(player_name):
#     def_data = {'overall_stat': 20, 'm_games': 0, 'm_win': 0, 'm_average': 0, 'm_record': 0,
#                 'b_games': 0, 'b_win': 0, 'b_average': 0}
#     with open('data.json') as f:        # считываем весь файл в переменную и закрываем, что бы не было "наслоений"
#         all_file_data = json.load(f)
#         f.close()
#     with open('data.json', 'w') as f:
#         while True:
#             if all_file_data.get(player_name):
#                 print(f'\nИгрок "{player_name}" уже есть в базе, введите другое имя!')
#                 continue
#             else:
#                 player_data = all_file_data.get(player_name, def_data)
#                 all_file_data[player_name] = player_data
#                 f.seek(0)
#                 f.write(json.dumps(all_file_data, indent=4))
#                 f.close()
#                 print(f'\nИгрок "{player_name}" успешно записан!')
#                 break
#     return 0


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
        else:
            print(f'\nИгрок "{player_name}" не найден в базе игроков!')
            input('Нажмите ENTER для продолжения...')
            return 0

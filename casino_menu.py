import json
from casino_rules import magic
from casino_blackjack import blackjack
#import ast


def main():
    menu()


def menu():
    all_points = 0
    player_name = (input('Введите имя игрока: '))
    def_data = {'overall_stat': 0, 'm_all': 0, 'm_win': 0, 'm_koef': 0, 'm_rec': 0,
                'b_all': 0, 'b_win': 0, 'b_koef': 0}
    with open('data.json') as f:
        players_data = json.load(f)
        player_data = players_data.get(player_name, def_data)
    print('Главное меню:\
            \n  1. Игра Magic\
            \n  2. Игра Blackjack\
            \n  3. Посмотреть статистику\
            \n  4. Сбросить игровой прогресс\
            \n  5. Выход')
    menu = input('Выберите действие: ')
    if menu == '1':
        magic(all_points)
        main()
    elif menu == '2':
        blackjack()
        main()
    elif menu == '3':
        pass
    elif menu == '4':
        pass
    elif menu == '5':
        exit('Выходим...')
    else:
        print('Выберите правильную цифру пункта меню!')
        main()


# def read_1(p_name):
#     pass
#     with open('data.json', 'r', encoding='utf-8') as f:
#          data_1 = json.load(f)
#          print(data_1)
#          for key in data_1.keys():
#              if key == p_name:
#                  print('Игрок уже в базе')
#              else:
#                  print('Игрок записан')


# def rw_file(data):
#     p_val1 = 0
#     m_val1 = m_val2 = m_val3 = m_val4 = 0
#     b_val1 = b_val2 = b_val3 = 0
#     def_data = {'data': {'overall_stat': p_val1, 'm_all': m_val1, 'm_win': m_val2, 'm_koef': m_val3, 'm_rec': m_val4,
#                       'b_all': b_val1, 'b_win': b_val2, 'b_koef': b_val3}}
#     with open('data.json', 'a', encoding='utf-8') as f:
#         json.dump(stats, f, ensure_ascii=False, indent=4)
#     print('Игрок записан')


def statistic():
    pass

#def testing():
#    with open('text.txt') as f:
#        text = f.read()
#    d = ast.literal_eval(text)
#    print(d)

if __name__ == "__main__":
    main()

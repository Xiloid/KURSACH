import json
from casino_magic import magic
from casino_blackjack import blackjack
import ast


def main():
    menu()


def menu():
    all_points = 0
    rw_file(input('Введите имя игрока: '))
    print('Главное меню:\
            \n  1. Игра Magic\
            \n  2. Игра Blackjack\
            \n  3. Посмотреть статистику\
            \n  4. Сбросить игровой прогресс\
            \n  5. Выход')
    print('\n Выберите действие: ')
    menu = input()
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


def rw_file(data):
    with open('data.json', 'w+', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print('Игрок записан')


#def testing():
#    with open('text.txt') as f:
#        text = f.read()
#    d = ast.literal_eval(text)
#    print(d)

if __name__ == "__main__":
    main()

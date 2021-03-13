from casino_magic import magic
from casino_blackjack import blackjack
from casino_rules import rules_magic, rules_bj
from casino_erase_stat import stat, erase


def main():
    player_name = input('Добро пожаловать в казино! Введите Ваше имя: ')
    menu(player_name)


def menu(player_name):
    print('\nГлавное меню:\
                \n  1. Игра Magic\
                \n  2. Игра BlackJack\
                \n  3. Посмотреть статистику\
                \n  4. Сбросить игровой прогресс\
                \n  5. Прочитать правила игр\
                \n  6. Выход')
    choice = input(f'\n {str.capitalize(player_name)}, выберите действие: ')
    if choice == '1':
        magic(player_name)
        menu(player_name)
    elif choice == '2':
        blackjack(player_name)
        menu(player_name)
    elif choice == '3':
        stat(player_name)
        menu(player_name)
    elif choice == '4':
        erase(player_name)
        menu(player_name)
    elif choice == '5':
        rules_magic()
        rules_bj()
        menu(player_name)
    elif choice == '6':
        exit('\nДо скорых встреч!')
    else:
        print('Выберите правильную цифру пункта меню!')
        menu(player_name)

if __name__ == "__main__":
    main()

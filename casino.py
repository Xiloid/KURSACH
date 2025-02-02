from casino_magic import magic
from casino_blackjack import blackjack
from casino_erase_stat import stat, erase
from colorama import Fore, Style
from colorama import init
init()


def main():
    player_name = input(Fore.LIGHTGREEN_EX + 'Добро пожаловать в казино! Введите Ваше имя: ' + Style.RESET_ALL)
    menu(player_name)


def menu(player_name):
    print(Fore.GREEN + '\nГлавное меню:\
                \n  1. Игра Magic\
                \n  2. Игра BlackJack\
                \n  3. Посмотреть статистику\
                \n  4. Сбросить игровой прогресс\
                \n  5. Прочитать правила игр\
                \n  6. Выход' + Style.RESET_ALL)
    choice = input(f'\n {str.capitalize(player_name)}, выберите действие и нажмите ENTER: ')
    if choice == '1':
        rules_magic()
        magic(player_name)
        menu(player_name)
    elif choice == '2':
        rules_bj()
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
        exit(Fore.BLUE + '\nДо скорых встреч!' + Style.RESET_ALL)
    else:
        print(Fore.RED + 'Выберите правильную цифру пункта меню!' + Style.RESET_ALL)
        menu(player_name)


def rules_magic():
    print(Fore.LIGHTYELLOW_EX + '''
            Правила игры "Magic":
            Изначально у Вас 20 очков.
            Компьютер загадывает число, а Вы должны угадать его за наименьшее число попыток.
            Зависимость начисления очков от количества попыток:
            Число угадано с 1й попытки - 20 очков
            Число угадано со 2й попытки - 15 очков
            Число угадано с 3й попытки - 10 очков
            Число угадано с 4й попытки - 5 очков
            Число угадано с 5й попытки - 0 очков
            Если Вы истратили все попытки, игра штрафует Вас на 5 очков. При нулевом или отрицательном балансе 
            очков - игра начисляет 20 очков. 
       \n''' + Style.RESET_ALL)
    input(Fore.BLUE + 'Нажмите ENTER для продолжения...' + Style.RESET_ALL)
    return 0


def rules_bj():
    print(Fore.LIGHTYELLOW_EX + '''
            Правила игры "BlackJack":
            Изначально у Вас 20 очков.
            Формируется колода из 56 карт, цель игры - вытянуть количествово карт соответствующее числу 21.
            Номиналы карт:
            От 2 до 10 - считаются аналогично
            Валет, Дама, Король - по 10 очков
            Туз - 11 очков, если сумма с тузом будет не больше 21, туз считается за 1 очко
            Вы делаете ставку, после чего игра начинается:
            Если Вы набираете 21 очко - ставка возвращается в удвоенном размере;
            Если Вы остановились на сумме меньше 21 - Ваша ставка возвращается;
            Если у Вас в сумме выходит больше 21 (перебор) - проигрыш (ставка снимается в пользу игры);
            При нулевом или отрицательном балансе очков - игра начисляет 20 очков.
       \n''' + Style.RESET_ALL)
    input(Fore.BLUE + 'Нажмите ENTER для продолжения...' + Style.RESET_ALL)
    return 0


if __name__ == "__main__":
    main()

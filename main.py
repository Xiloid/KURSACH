#import random
#from magic import magic
#from blackjack import blackjack
import colorama
colorama.init()
from colorama import Fore, Style


def main():
    all_points = 0
    print(Fore.GREEN + "Главное меню:\
        \n  1. Игра Magic\
        \n  2. Игра Blackjack\
        \n  3. Посмотреть статистику\
        \n  4. Сбросить игровой прогресс\
        \n  5. Виход", Style.RESET_ALL)
    print(Fore.BLUE + "\n Выберите действие: ", Style.RESET_ALL)
    menu = input()
    if menu == "1":
        pass
    elif menu == "2":
        pass
    elif menu == "3":
        pass
    elif menu == "4":
        pass
    elif menu == "5":
        exit('Выходим...')
    else:
        print(Fore.YELLOW + 'Выберите правильную цифру пункта меню!', Style.RESET_ALL)
        main()


if __name__ == "__main__":
    main()

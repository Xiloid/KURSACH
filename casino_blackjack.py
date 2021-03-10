import random


def main():
    blackjack()


def blackjack():
    while True:
        start = input('\nНажмите Enter что бы начать или введите "q" для выхода \n')
        # тут переменная ставки в размере не большем, чем общее количетсво очков
        if start != 'q':
            deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
            count = 0
            random.shuffle(deck)

            while True:
                choice = input('\nЕщё карту: "y" Если хватит: "n" ')
                if choice == 'y':
                    current = deck.pop()
                    if current == 11 and count > 10:
                        current = 1
                        print(f'\nВыпал "Туз", и т.к. на руках {count} очков, трактуем его как 1')
                    count += current
                    print(f'\nВам попалась карта достоинством {current}, теперь у вас {count} очков')
                    if count > 21:
                        print('\nК сожалению у Вас перебор!')
                        # проигрыш (ставка снимается в пользу казино)
                        break
                    elif count == 21:
                        print(f'\nПоздравляем, Вы выиграли! Ваша ставка {None} возвращена в удвоенном размере!')
                        # ставка = ставка * 2
                        # игроку возвращается удвоенная ставка
                        break
                else:
                    print(f'\nПас! На руках {count} очков. Ваша ставка {None} возвращена')
                    # записываем очки обратно и закрываем файл?
                    # ставка возвращается игроку
                    break
        else:
            break
        print('\nПока!')
        # возврат в меню


if __name__ == "__main__":
    main()

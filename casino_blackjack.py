import random


def blackjack():
    while True:
        start = input('Нажмите Enter что бы начать, для выхода введите Exit \n')
        start = start.lower()
        if start != 'exit':
            deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
            count = 0
            croupier_count = 0
            # перемешали колоду
            random.shuffle(deck)
            # переменные для крупье
            croupier_current = deck.pop()
            croupier_count += croupier_current
            print('У крупье {} очков'.format(croupier_current))
            print('Добро пожаловать в игру 21!: ')

            while True:

                choise = input('У вас {} очков, что бы взять карту нажмите y или n что бы остановиться: '.format(count))
                choise = choise.lower()

                if choise == 'y':
                    current = deck.pop()
                    print('Вам попалась карта достоинством {}'.format(current))
                    count += current
                    if count > 21:
                        print('У вас перебор')
                        break
                    elif count == 21:
                        print('Вы выиграли')
                        break
                    else:
                        print('')
                else:
                    print('У вас {} очков, крупье берет карту: '.format(count))
                    # блок добора и сравнения карт крупье
                    while True:
                        if croupier_count >= 17:
                            if count <= croupier_count <= 21:
                                print('Вы проиграли!, у вас {} у крупье {}'.format(count, croupier_count))
                                break
                            else:
                                print('Вы выиграли, набрав {} очков'.format(count))
                                break
                        else:
                            if croupier_count < 17:
                                croupier_current = deck.pop()
                                croupier_count += croupier_current
                                print('Крупье взял еще и ему выпало {}, у крупье {}'.format(croupier_current,
                                                                                          croupier_count))
                    break
        else:
            break
        print('quit')

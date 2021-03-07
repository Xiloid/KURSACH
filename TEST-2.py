import random

random_number = random.randint(1, 10)
counter = 1
number = 0
print("Компьютер загадал число. Отгадайте его. У вас 5 попыток")
while counter <= 5:
    try:
        number = int(input(str(counter) + '-я попытка: '))
    except ValueError:
        print('Должно быть целое число!')
        continue
    if number > random_number:
        print('Много')
    elif number < random_number:
        print('Мало')
    else:
        print(f'Вы угадали с {counter}-й попытки')
        break
    counter += 1
else:
    print(f'Вы исчерпали 5 попыток. Было загадано число {random_number}')

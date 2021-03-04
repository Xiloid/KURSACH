import random
import main

def magic(all_points):
#    rules()
    random_number = random.randint(1, 10)
    print("Вгадайте Магічне число від 1 до 10")
    counter = 0
    print("==Ігра починається==\n")
    while True:
        try:
            number = int(input("Ваше число: "))
            counter += 1
        except ValueError:
            print("Це повинно бути число.")
            continue
        if number > random_number:
            print("Магічне число менше", number)
        elif number < random_number:
            print("Магічне число більше", number)
        else:
            print("\nВітаю! Ви вгадали число",number,"")
            print("Витрачено спроб:", counter)
            random_number = random.randint(1, 10)
            points_1 = 0
            if counter == 1:
                print(f"Вам начисляно 50 очків")
                points_1 = 50
            elif counter == 2:
                print("Вам начисляно 25 очків")
                points_1 = 25
            elif counter == 3:
                print("Вам начисляно 10 очків")
                points_1 = 10
            elif counter == 4:
                print("Вам начисляно 5 очків")
                points_1 = 5
            else:
                print("Вам начисляно 0 очків")

            if all_points == 0:
                all_points = points_1
            else:
                all_points += points_1
            print("Тепер у вас",all_points,"очків")
            break

        if counter == 5:
            print("\nМагічне число було",random_number)
            print("Використано забагато спроб")
            break
    next_action = input("\nСпробувати ще раз?(y/n/menu):")
    if next_action == "Y":
        counter = 0
        magic(all_points)
    elif next_action == "menu":
        main()
    return all_points

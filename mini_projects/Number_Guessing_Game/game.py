import random

print("Добро пожаловать в числовую угадайку")

def is_valid(string, n):
    return string.isdigit() and 1 <= int(string) <= n


while True:
    n = int(input("Введите максимальное число: "))
    comp_number = random.randint(1, n)
    count = 0

    while True:
        user_number = input(f"Угадай число от 1 до {n}: ")

        if is_valid(user_number, n):
            user_number = int(user_number)
            count += 1

            if user_number < comp_number:
                print("Ваше число меньше загаданного, попробуйте еще разок")
            elif user_number > comp_number:
                print("Ваше число больше загаданного, попробуйте еще разок")
            else:
                print("Вы угадали, поздравляем!")
                print(f"Количество попыток: {count}")
                break
        else:
            print(f"А может быть введем целое число от 1 до {n}?")

    again = input("Хотите сыграть еще раз? (да/нет): ").lower()
    if again != "да":
        break

print("Спасибо, что играли в числовую угадайку. Еще увидимся...")
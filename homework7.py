from langdetect import detect
import random


# Задание 1 'Быки и коровы':

def generate_number():
    digits = list(range(10))
    random.shuffle(digits)
    if digits[0] == 0:
        digits[0], digits[1] = digits[1], digits[0]
    return digits[:4]


def check_guess(number, guess):
    bulls = 0
    cows = 0
    for i in range(4):
        if guess[i] == number[i]:
            bulls += 1
        elif guess[i] in number:
            cows += 1
    return bulls, cows


def play_game():
    print('Игра \'Быки и коровы\'\n'
          'Правила игры:\n'
          'Ваша задача - отгадать загаданное компьютером 4-значное число.\n'
          'После каждой попытки компьютер сообщит вам, сколько цифр угадано без совпадения с их позициями в '
          'загаданном числе (коровы) и сколько угадано вплоть до позиций в загаданном числе (быки).')

    number = generate_number()
    attempts = 0

    while True:
        guess = input('Введите 4-значное число с неповторяющимися цифрами: ')

        if len(guess) != 4 or not guess.isdigit():
            print('Пожалуйста, введите 4-значное число.')
            continue

        guess = list(map(int, guess))

        if len(set(guess)) != 4:
            print('Пожалуйста, введите число с неповторяющимися цифрами.')
            continue

        attempts += 1

        bulls, cows = check_guess(number, guess)
        print('Быки: ', bulls)
        print('Коровы: ', cows)

        if bulls == 4:
            print('Вы выиграли!')
            break

        print()

    print('Загаданное число: ', ''.join(map(str, number)))
    print('Количество попыток: ', attempts)


play_game()


# Задание 2 'Like':

def like_count(names):
    num_likes = len(names)
    lang = detect(names[0])
    if lang == 'ru':
        if num_likes == 1:
            return f'{names[0]} нравится это'
        elif num_likes == 2:
            return f'{names[0]} и {names[1]} нравится это'
        elif num_likes == 3:
            return f'{names[0]}, {names[1]} и {names[2]} нравится это'
        elif num_likes > 3:
            return f'{names[0]}, {names[1]} и еще {num_likes - 2} человек нравится это'
        else:
            return 'Никому это не нравится'
    elif lang == 'en':
        if num_likes == 1:
            return f'{names[0]} likes this'
        elif num_likes == 2:
            return f'{names[0]} and {names[1]} like this'
        elif num_likes == 3:
            return f'{names[0]}, {names[1]}, and {names[2]} like this'
        elif num_likes > 3:
            return f'{names[0]}, {names[1]}, and {num_likes - 2} others like this'
        else:
            return 'No one likes this'


names = input('Введите имена через запятую: ').split(',')

print(like_count(names))

# Задание 3 'BuzzFuzz':

lower = 0
upper = 0

while lower <= 0:
    lower = int(input('Введите начало интервала (должен быть положительным числом): '))
    if lower <= 0:
        print('Начало интервала должно быть положительным числом, повторите ввод.')

while upper <= lower:
    upper = int(input('Введите конец интервала (должен быть больше начала интервала): '))
    if upper <= lower:
        print('Конец интервала должен быть больше начала интервала, повторите ввод.')

for i in range(lower, upper + 1):
    if i % 3 == 0 and i % 5 == 0:
        print('FuzzBuzz')
    elif i % 3 == 0:
        print('Fuzz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)

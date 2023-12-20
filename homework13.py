import re
import os

# Задание "Re: 1":
# Напишите программу, которая будет считывать строки из текстового файла и находить все даты в формате "dd.mm.yyyy".
# Выведите найденные даты на экран.


def find_dates(file_path):
    pattern = r"\d{2}\.\d{2}\.\d{4}\b"

    if os.path.isdir(file_path):
        for dir_path, dir_names, file_names in os.walk(file_path):
            for file_name in file_names:
                if file_name.endswith(".txt"):
                    file_path = os.path.join(dir_path, file_name)
                    with open(file_path, "r") as file:
                        content = file.read()
                    dates = re.findall(pattern, content)
                    if dates:
                        print("Найденные даты в файле", file_path, ":")
                        for date in dates:
                            print(date)

    else:
        with open(file_path, "r") as file:
            content = file.read()
        dates = re.findall(pattern, content)
        if dates:
            print("Найденные даты в файле", file_path, ":")
            for date in dates:
                print(date)


file_path = input("Введите путь к текстовому файлу или каталогу: ")
find_dates(file_path)


# Задание "Re: 2":
# Разработайте программу для проверки корректности паролей.
# Пароль считается корректным, если он содержит не менее 8 символов,
# включает хотя бы одну заглавную букву, одну строчную букву и одну цифру.

def check_password(password):
    if len(password) < 8:
        return False
    if not re.search("[A-Z]", password) or not re.search("[a-z]", password) or not re.search("[0-9]", password):
        return False
    return True


while True:
    password = input("Введите пароль: ")
    if check_password(password):
        print("Пароль корректный.")
        break
    else:
        print("Пароль некорректный. Повторите ввод:")
        continue


# Задание "Re: 3":
# В предложении допущены ошибки. Необходимо исправить каждый такой повтор
# (слово, один или несколько пробельных символов, и снова то же слово).

sentence = "Довольно распространённая ошибка ошибка — это лишний повтор повтор слова слова. " \
           "Смешно, не не правда ли? " \
           "Не нужно портить хор хоровод."

fixed_sentence = re.sub(r'(\b\w+\b)\s+\1', r'\1', sentence)
print(fixed_sentence)


# Задание "Iterator and generator *"
# Напишите программу, которая запрашивает у пользователя целое число N и создает
# генераторную функцию для генерации чисел от 1 до N. Выведите сумму всех чисел, сгенерированных этой функцией.
# Создайте генераторную функцию, которая генерирует все простые числа в заданном диапазоне. Выведите первые 10
# простых чисел из этого диапазона.

def generate_numbers(N):
    if N <= 0:
        raise ValueError("N должно быть положительным целым числом")
    for i in range(1, N + 1):
        yield i


try:
    N = int(input("Введите целое число N: "))
    numbers_gen = generate_numbers(N)
    sum_numbers = sum(numbers_gen)
    print("Сумма всех чисел:", sum_numbers)
except ValueError as e:
    print(e)


def generate_prime_numbers(start, end):
    if start < 2:
        raise ValueError("Начало диапазона должно быть не меньше 2")
    if end < start:
        raise ValueError("Конец диапазона должен быть больше или равен началу диапазона")

    count = 0
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                yield num
                count += 1
                if count == 10:
                    break

    if count < 10:
        raise ValueError("В диапазоне должно быть минимум 10 простых чисел")


try:
    start_range = int(input("Введите начало диапазона: "))
    while True:
        end_range = int(input("Введите конец диапазона: "))
        if start_range <= end_range:
            break
        else:
            print("Начало диапазона больше конца диапазона. Повторите ввод.")

    prime_numbers_gen = generate_prime_numbers(start_range, end_range)

    print("Первые 10 простых чисел из диапазона:")
    for num in prime_numbers_gen:
        print(num)

except ValueError as e:
    print(e)

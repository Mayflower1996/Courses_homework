"""Homework 9: Recursive Functions."""


# Задание 1 'Строки с заданным символом'

def remove_previous_char(s):
    """Remove the character '#' and the character preceding it recursively."""
    index = s.find('#')
    if index != -1:
        if index == 0:
            s = s[1:]
        else:
            s = s[:index - 1] + s[index + 1:]
        return remove_previous_char(s)
    else:
        return s


string = input('Введите строку: ')

print(remove_previous_char(string))


# Задание 2 'Рекурсия'

def countdown(n):
    """Print numbers from n to 1, then from 1 to n using recursion."""
    if n < 1:
        print(n)
        countdown(n + 1)
    else:
        print(n)
        if n > 1:
            countdown(n - 1)


while True:
    try:
        n = int(input('Введите число n: '))
        countdown(n)
        break
    except ValueError:
        print('Введено некорректное значение. Пожалуйста, введите число.')
        continue

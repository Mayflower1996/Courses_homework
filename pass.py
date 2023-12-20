import re


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

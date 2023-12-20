# Задание 1 "Validate":

def validate(card_number):
    if not card_number.isdigit():
        return False

    if len(card_number) < 7 or len(card_number) > 19:
        return False

    digits = [int(x) for x in card_number]

    if len(digits) % 2 == 0:
        even = True
    else:
        even = False

    for i in range(len(digits) - 2, -1, -2 if even else -2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9

    total = sum(digits)

    if total % 10 == 0:
        return True
    else:
        return False


while True:
    card_number = input("Введите номер карты (может быть длиной от 7 до 19 цифр): ")
    card_number = card_number.strip()

    if not card_number.isdigit():
        print("Ошибка! Введите только цифры.")
        continue

    result = validate(card_number)
    print(result)
    break


# Задание 2 "Подсчет количества букв"

def compress_string(string):
    compressed = ""
    count = 1
    for i in range(len(string)):
        if i == len(string) - 1 or string[i] != string[i + 1]:
            if count == 1:
                compressed += string[i]
            else:
                compressed += string[i] + str(count)
            count = 1
        else:
            count += 1
    return compressed


input_string = input("Введите строку: ")
compressed_string = compress_string(input_string)
print("Сжатая строка:", compressed_string)

# Задание 1
# Заменить символ "#" на символ "/" в строке 'www.my_site.com#about'

str = 'www.my_site.com#about'
new_str = str.replace("#", "/")
print(new_str)


# Задание 2
# Напишите программу, которая добавляет 'ing' к словам

while True:
    word = input("Enter a single word: ")
    if not word.isalpha():
        print("Invalid input. Please enter a single word.")
        continue
    elif word.endswith("ing"):
        print("The word already ends with 'ing'")
        break
    elif word.endswith("e"):
        word_with_ing = word[:-1] + "ing"
        print("Word with added 'ing':", word_with_ing)
        break
    elif len(word) >= 2 and word[-3:] not in ['ing', 'e'] and word[-2:] not in ['ie']:
        word_with_ing = word + "ing"
        print("Word with added 'ing':", word_with_ing)
        break
    else:
        word_with_ing = word
        print("Word with added 'ing':", word_with_ing)
        break


# Задание 3
# В строке "Ivanou Ivan" поменяйте местами слова => "Ivan Ivanou"

string = "Ivanou Ivan"
words = string.split()
reversed_string = " ".join([words[1], words[0]])
print("Original string:", string)
print("Changed string:", reversed_string)


# Задание 4
# Напишите программу которая удаляет пробел в начале, в конце строки

string = input("Enter the string: ")
string = string.strip()
print("Spaces have been removed:", string)

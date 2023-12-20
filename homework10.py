# Задание 1 "Положительные аргументы функции":

def validate_arguments(func):
    def wrapper(*args):
        for arg in args:
            if not isinstance(arg, int) or arg < 0:
                raise ValueError("Ошибка! Аргумент должен быть положительным числом.")
        return func(*args)

    return wrapper


@validate_arguments
def calculate_sum(a, b):
    return a + b


result = calculate_sum(5, -10)


# Задание 2 "Вернуть число":

def check_result(func):
    def wrapper(*args):
        if not all(isinstance(arg, (int, float)) for arg in args):
            print("Ошибка! Аргументы функции должны быть числами.")
        else:
            result = func(*args)
            if not isinstance(result, (int, float)):
                print("Ошибка! Результат функции не является числом.")
            else:
                return result

    return wrapper


@check_result
def add_numbers(a, b):
    return a + b


result = add_numbers(10, 20)
print(result)
result = add_numbers("10", "20")


# Задание 3 "Декоратор типов":

def typed(type):
    def decorator(func):
        def wrapper(*args):
            new_args = []
            for arg in args:
                if isinstance(arg, type):
                    new_args.append(arg)
                else:
                    try:
                        new_args.append(type(arg))
                    except ValueError:
                        raise TypeError(f"Аргумент {arg} невозможно привести к типу {type}")
            return func(*new_args)

        return wrapper

    return decorator


@typed(type=str)
def add(a, b):
    return a + b


result = add("3", 5)
print(result)

result = add(5, 5)
print(result)

result = add('a', 'b')
print(result)


@typed(type=int)
def add(a, b, c):
    return a + b + c


result = add("5", 6.0, 7)
print(result)


@typed(type=float)
def add(a, b, c):
    return a + b + c


result = add("0.1", 0.2, 0.4)
print(result)


# Задание 4 "Функция кэширования*":

cache_dict = {}


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def cache(func):
    def wrapper(n):
        if n in cache_dict:
            print(f"Значение {cache_dict[n]} было взято из кэша.")
        else:
            result = func(n)
            cache_dict[n] = result
            print(f"Значение {cache_dict[n]} было добавлено в кэш.")

    return wrapper


@cache
def fib(n):
    x = fibonacci(n)
    return x


fib(10)
fib(5)
fib(10)
fib(5)

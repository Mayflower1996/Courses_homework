"""
Homework 10: Decorators and Caching.
"""


# Задание 1 'Положительные аргументы функции':

def validate_arguments(func):
    """
    Validate if arguments are positive integers.
    """

    def wrapper(*args):
        """
        Validate arguments.
        """
        for arg in args:
            if not isinstance(arg, int) or arg < 0:
                raise ValueError('Ошибка! Аргумент должен быть положительным числом.')
        return func(*args)

    return wrapper


@validate_arguments
def calculate_sum(a, b):
    """
    Calculate the sum of two numbers.
    """
    return a + b


result = calculate_sum(5, 10)


# Задание 2 'Вернуть число':

def check_result(func):
    """
    Check if function arguments and return value are numbers.
    """

    def wrapper(*args):
        """
        Check arguments and return value.
        """
        if not all(isinstance(arg, (int, float)) for arg in args):
            raise ValueError('Ошибка! Аргументы функции должны быть числами.')

        result = func(*args)
        if not isinstance(result, (int, float)):
            raise ValueError('Ошибка! Результат функции не является числом.')

        return result

    return wrapper


@check_result
def add_numbers(a, b):
    """
    Add two numbers.
    """
    return a + b


result = add_numbers(10, 20)
print(result)


# result = add_numbers('10', '20')  # Ошибка, строковые аргументы


# Задание 3 'Декоратор типов':

def typed(type):
    """
    Enforce argument types for a function.
    """

    def decorator(func):
        """
        Decorate to enforce argument types.
        """

        def wrapper(*args):
            """
            Enforce argument types.
            """
            new_args = []
            for arg in args:
                if isinstance(arg, type):
                    new_args.append(arg)
                else:
                    try:
                        new_args.append(type(arg))
                    except ValueError:
                        raise TypeError(f'Аргумент {arg} невозможно привести к типу {type}')
            return func(*new_args)

        return wrapper

    return decorator


@typed(type=str)
def add_str(a, b):
    """
    Concatenate two strings.
    """
    return a + b


result = add_str('3', '5')
print(result)


@typed(type=int)
def add_int(a, b, c):
    """
    Add three integers.
    """
    return a + b + c


result = add_int(5, 6, 7)
print(result)


@typed(type=float)
def add_float(a, b, c):
    """
    Add three floating-point numbers.
    """
    return a + b + c


result = add_float(0.1, 0.2, 0.4)
print(result)

# Задание 4 'Функция кэширования*':

cache_dict = {}


def fibonacci(n):
    """
    Compute the Fibonacci sequence up to n.
    """
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def cache(func):
    """
    Cache function results.
    """

    def wrapper(n):
        """
        Check cache for results.
        """
        if n in cache_dict:
            print(f'Значение {cache_dict[n]} было взято из кэша.')
        else:
            result = func(n)
            cache_dict[n] = result
            print(f'Значение {cache_dict[n]} было добавлено в кэш.')

    return wrapper


@cache
def fib(n):
    """
    Compute the nth Fibonacci number using caching.
    """
    x = fibonacci(n)
    return x


fib(10)
fib(5)
fib(10)
fib(5)

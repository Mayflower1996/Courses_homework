"""Homework 11: Library & Deposit."""


# Задание 1 'Библиотека':

class Book:
    """Representing a book with reservation and borrowing functionalities."""

    def __init__(self, name, author, pages, isbn):
        """Initialize a Book object with name, author, pages, and isbn."""
        self.name = name
        self.author = author
        self.pages = pages
        self.isbn = isbn
        self.reserved = False
        self.borrowed = False
        self.user = None

    def reserve(self, user):
        """Reserves the book for a user."""
        if self.borrowed:
            print('Книга уже взята другим пользователем')
        elif self.reserved:
            print('Книга уже зарезервирована')
        else:
            self.reserved = True
            self.user = user
            print(f"Книга '{self.name}' зарезервирована пользователем {user.name}")

    def cancel_reservation(self, user):
        """Cancel the reservation of the book for a user."""
        if not self.reserved:
            print('У вас нет зарезервированных книг')
        elif self.user != user:
            print('Нельзя отменить резервирование за другого пользователя')
        else:
            self.reserved = False
            self.user = None
            print(f"Резервирование книги '{self.name}' отменено")

    def borrow(self, user):
        """Allow a user to borrow the book."""
        if self.borrowed:
            print('Книга уже взята')
        elif self.reserved and self.user != user:
            print('Книга зарезервирована другим пользователем')
        else:
            self.borrowed = True
            self.user = user
            print(f"Книга '{self.name}' взята пользователем {user.name}")

    def return_book(self, user):
        """Return the book by a user."""
        if not self.borrowed:
            print('У вас нет взятых книг')
        elif self.user != user:
            print('Нельзя вернуть книгу за другого пользователя')
        else:
            self.borrowed = False
            self.user = None
            print(f"Книга '{self.name}' возвращена")


class User:
    """Representing a user of the library."""

    def __init__(self, name):
        """Initialize a User object with a name."""
        self.name = name

    def change_user(self, new_user):
        """Change the current user."""
        global current_user
        current_user = new_user


book1 = Book('Book 1', 'Author 1', 200, 'ISBN1')
book2 = Book('Book 2', 'Author 2', 150, 'ISBN2')
book3 = Book('Book 3', 'Author 3', 300, 'ISBN3')
book4 = Book('Book 4', 'Author 4', 250, 'ISBN4')
book5 = Book('Book 5', 'Author 5', 180, 'ISBN5')

user1 = User('User1')
user2 = User('User2')

current_user = user1

while True:
    print('--- МЕНЮ ---')
    print('1. Взять книгу')
    print('2. Вернуть книгу')
    print('3. Зарезервировать книгу')
    print('4. Отменить резервирование книги')
    print('5. Сменить пользователя')
    print('6. Выход')

    choice = input('Выберите действие (1-6): ')

    if choice == '1':
        book = int(input('Введите номер книги (1-5): '))
        if book == 1:
            book1.borrow(current_user)
        elif book == 2:
            book2.borrow(current_user)
        elif book == 3:
            book3.borrow(current_user)
        elif book == 4:
            book4.borrow(current_user)
        elif book == 5:
            book5.borrow(current_user)
    elif choice == '2':
        book = int(input('Введите номер книги (1-5): '))
        if book == 1:
            book1.return_book(current_user)
        elif book == 2:
            book2.return_book(current_user)
        elif book == 3:
            book3.return_book(current_user)
        elif book == 4:
            book4.return_book(current_user)
        elif book == 5:
            book5.return_book(current_user)
    elif choice == '3':
        book = int(input('Введите номер книги (1-5): '))
        if book == 1:
            book1.reserve(current_user)
        elif book == 2:
            book2.reserve(current_user)
        elif book == 3:
            book3.reserve(current_user)
        elif book == 4:
            book4.reserve(current_user)
        elif book == 5:
            book5.reserve(current_user)
    elif choice == '4':
        book = int(input('Введите номер книги (1-5): '))
        if book == 1:
            book1.cancel_reservation(current_user)
        elif book == 2:
            book2.cancel_reservation(current_user)
        elif book == 3:
            book3.cancel_reservation(current_user)
        elif book == 4:
            book4.cancel_reservation(current_user)
        elif book == 5:
            book5.cancel_reservation(current_user)
    elif choice == '5':
        new_user = input('Введите имя пользователя: ')
        current_user.change_user(User(new_user))
    elif choice == '6':
        break


# Задание 2 'Банковский вклад':

class Deposit:
    """Representing a bank deposit with interest calculation."""

    def __init__(self, amount, duration):
        """Initialize a Deposit object with amount and duration."""
        self.amount = amount
        self.duration = duration

    def calculate_interest(self):
        """Calculate the total amount with interest."""
        monthly_interest_rate = 0.1 / 12
        total_amount = self.amount
        for _ in range(self.duration * 12):
            total_amount += total_amount * monthly_interest_rate
        return total_amount


class Bank:
    """Representing a bank where a user can make deposits."""
    @staticmethod
    def deposit():
        """Accept user input for deposit amount and duration."""
        amount = float(input('Введите сумму: '))
        duration = int(input('Введите срок (в годах): '))
        deposit = Deposit(amount, duration)
        return deposit.calculate_interest()


bank = Bank()
total_amount = bank.deposit()
print('Сумма на счету через заданный срок:', total_amount)

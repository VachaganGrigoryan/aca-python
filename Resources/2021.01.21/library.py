class Book:

    def __init__(self, isbn: str, title: str, authors: list):
        if not isinstance(authors, (list, tuple)):
            raise TypeError('Authors must be either list or tuple')

        self.isbn = isbn
        self.title = title.title()
        self.authors = tuple(map(str.title, authors))

    def to_string(self) -> str:
        return f'Book(isbn={self.isbn}, title={self.title}, authors={", ".join(self.authors)})'


class BookCollection:

    def __init__(self):
        self.storage = {}

    def add(self, book: Book):
        if not isinstance(book, Book):
            raise TypeError('Book instance is expected')
            
        if book.isbn in self.storage:
            self.storage[book.isbn]['count'] += 1
        else:
            self.storage[book.isbn] = {
                'count': 1,
                'book': book
            }

    def show(self):
        for idx, (isbn, record) in enumerate(self.storage.items(), start=1):
            print(idx, '.', record['book'].to_string(), '-', record['count'])


class Application:

    COMMANDS: tuple = (
        'add-book',
        'remove-book',
        'borrow-book',
        'show-book',
        'show-books',
        'exit'
    )

    def __init__(self):
        self.collection = BookCollection()
        self.__exit = False

    def run(self):
        commands = Application.COMMANDS

        while not self.__exit:
            cmd = input('command: ').lower().strip()
            if cmd not in commands:
                print('[ERROR] Invalid command')
                continue

            try:
                getattr(self, cmd.replace('-', '_'))()
            except TypeError as tex:
                print('[ERROR]', str(tex))

            print()
        
    def add_book(self):
        isbn = input('ISBN: ').strip()
        title = input('Title: ').strip()
        authors = input('Authors: ').strip().split(',')

        self.collection.add(Book(isbn, title, authors))

    def remove_book(self):
        pass

    def borrow_book(self):
        pass

    def show_book(self):
        pass

    def show_books(self):
        self.collection.show()

    def exit(self):
        self.__exit = True


if __name__ == '__main__':
    Application().run()

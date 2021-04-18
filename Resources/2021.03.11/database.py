import sqlite3

from typing import Union
from collections import namedtuple
from abc import ABC, abstractmethod
from contextlib import contextmanager


def namedtuple_factory(cursor, row):
    pass


class DBSession:

    __slots__ = 'conn', 'in_transaction'

    def __init__(self, dbpath: str):
        self.conn = sqlite3.connect(dbpath)
        self.conn.row_factory = sqlite3.Row
        self.in_transaction = False

    def __del__(self):
        self.conn.close()

    def execute(self, query: str, params: Union[list, tuple, dict] = None):
        cursor = self.conn.cursor()
        cursor.execute(query, params or tuple())
        if not self.in_transaction:
            self.conn.commit()
        return cursor

    def find(self, query: str, params: Union[list, tuple, dict] = None):
        cursor = self.execute(query, params)
        result = cursor.fetchone()
        cursor.close()
        return result

    def delete(self, table: str, where: str, values: Union[list, tuple, dict] = None):
        # NOTE: this is not a safe function
        if where:
            query = f"DELETE FROM `{table}` WHERE {where};"
        else:
            query = f"DELETE FROM `{table}`;"

        self.execute(query, values)

    @contextmanager
    def transaction(self):
        try:
            self.in_transaction = True
            yield
            self.conn.commit()
        except sqlite3.DatabaseError as dbex:
            self.conn.rollback()
            raise dbex
        finally:
            self.in_transaction = False


class Application:

    def __init__(self, session: DBSession):
        self.session = session

    def __del__(self):
        del self.session

    def run(self):
        # Authors(self.session).add('Avetik', 'Isahakyan')
        '''Books(self.session).add(
            'Dog and Cat',
            'Tale',
            namedtuple('Author', ('first_name', 'last_name'))('Hovhannes', 'Tumanyan')
        )'''
        '''Books(self.session).add(
            'C Programming Language',
            'Engineering',
            namedtuple('Author', ('first_name', 'last_name'))('Dennis', 'Ritchie')
        )'''
        for idx, author in enumerate(Authors(self.session).get(), start=1):
            print(idx, '# ', author['first_name'], ' ', author['last_name'], sep='')


class Model(ABC):

    def __init__(self, session: DBSession):
        super().__init__()
        self.session = session

    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def remove(self):
        pass


class Authors(Model):

    def add(self, first_name: str, last_name: str) -> int:
        result = self.session.execute(
            "INSERT INTO authors(first_name, last_name) VALUES (?, ?);",
            (first_name.upper(), last_name.upper())
        )
        row_id = result.lastrowid
        result.close()
        return row_id

    def get(self):
        return self.session.execute("SELECT * FROM authors ORDER BY id;")

    def remove(self, **kwargs):
        self.session.delete(
            'authors',
            ' AND '.join((f'`{key}` = ?' for key in kwargs)),
            tuple(map(lambda v: str(v).upper(), kwargs.values()))
        )

    def find_by_name(self, first_name: str, last_name: str):
        return self.session.find("""
            SELECT
                id
            FROM
                authors
            WHERE
                first_name LIKE :fname
                AND last_name LIKE :lname
            LIMIT 1;""",
            {
                'fname': first_name.upper(),
                'lname': last_name.upper()
            }
        )


class Books(Model):

    def add(self, title: str, genre: str, author):
        session = self.session
        authors = Authors(session)

        with session.transaction():
            found_author = authors.find_by_name(author.first_name, author.last_name)
            # author_id = found_author[0] if found_author else authors.add(author.first_name, author.last_name)
            author_id = found_author['id'] if found_author else authors.add(author.first_name, author.last_name)

            book_id = session.execute(
                "INSERT INTO books(title) VALUES (?)",
                (title,)
            ).lastrowid

            session.execute(
                "INSERT INTO book_authors(book_id, author_id) VALUES (?, ?)",
                (book_id, author_id)
            ).close()

    def remove(self, **kwargs):
        pass


if __name__ == '__main__':
    Application(DBSession('library.db')).run()

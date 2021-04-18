import sqlite3


class Author:

    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name


def add_book(title: str, genre: str, author: Author):
    global conn
    
    cursor = conn.cursor()
    try:
        cursor.execute(
            """SELECT
                id
            FROM
                authors
            WHERE
                first_name LIKE :fname
                AND last_name LIKE :lname
            LIMIT 1;""",
            {
                'fname': author.first_name,
                'lname': author.last_name
            }
        )

        found_author = cursor.fetchone()
        author_id = found_author[0] if found_author else add_author(author)

        cursor.execute("INSERT INTO books(title) VALUES (?)", (title,))
        book_id = cursor.lastrowid

        cursor.execute(
            "INSERT INTO book_authors(book_id, author_id) VALUES (?, ?)",
            (book_id, author_id)
        )
        
        conn.commit()
    except sqlite3.DatabaseError as dbex:
        conn.rollback()
        print('[ERROR]', str(dbex))
    finally:
        cursor.close()


def add_author(author: Author) -> int:
    global conn
    
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO authors(first_name, last_name) VALUES (?, ?);",
            (author.first_name, author.last_name)
        )

        return cursor.lastrowid
    finally:
        cursor.close()


if __name__ == '__main__':
    conn = sqlite3.connect('library.db')
    try:
        add_book('Dog and Cat', 'Tale', Author('Hovhannes', 'Tumanyan'))
    finally:
        conn.close()

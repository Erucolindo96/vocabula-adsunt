import sqlite3
from typing import List

from config import config
from database.entities.Book import Book
from database.entities.Age import Age
from database.entities.Author import Author


class BookDao:
    def __init__(self):
        pass

    def get_by_id(self, book_id: int) -> Book:
        connection = sqlite3.connect(config.database['path'])
        cursor = connection.cursor()

        cursor.execute('SELECT book.id, title, uri, author.id, author.name, '
                       'age.id, age.name FROM book '
                       'LEFT OUTER JOIN author ON author.id = book.author_id '
                       'LEFT OUTER JOIN age ON age.id = book.age_id '
                       'WHERE book.id = :id', {'id': book_id})
        row = cursor.fetchone()

        connection.commit()
        connection.close()
        age = Age(row[5], row[6]) if row else None
        author = Author(row[3], row[4]) if row else None

        return Book(row[0], row[1], row[2], age, author) if row else None

    def list_by_title(self, book_title: str) -> List[Book]:
        connection = sqlite3.connect(config.database['path'])
        cursor = connection.cursor()

        cursor.execute('SELECT id, title, uri, author.id, author.name, '
                       'age.id, age.name FROM book '
                       'LEFT OUTER JOIN author ON author.id = book.author_id'
                       'LEFT OUTER JOIN age ON age.id = book.age_id '
                       'WHERE book.title like :title',
                       {'title': '%' + book_title + '%'})
        data = cursor.fetchall()

        book_list = []
        for row in data:
            age = Age(row[5], row[6]) if row else None
            author = Author(row[3], row[4]) if row else None
            book_list.append(Book(row[0], row[1], row[2], age, author))

        connection.commit()
        connection.close()

        return book_list

    def fetch_content(self, book: Book) -> Book:
        connection = sqlite3.connect(config.database['path'])
        cursor = connection.cursor()

        cursor.execute('SELECT content FROM book '
                       'WHERE book.id = :id', {'id': book.get_id()})
        row = cursor.fetchone()

        connection.commit()
        connection.close()

        book.set_content(row[0])
        return book

    def insert(self, book: Book) -> None:
        connection = sqlite3.connect(config.database['path'])
        cursor = connection.cursor()

        author = book.get_author()
        age = book.get_age()
        author_id = author.get_id() if author else None
        age_id = age.get_id() if age else None

        cursor.execute('INSERT INTO '
                       'book(title, content, uri, author_id, age_id) '
                       'VALUES '
                       '(:title, :content, :uri, :author_id, :age_id)',
                       {'title': book.get_title(),
                        'content': book.get_content(), 'uri': book.get_uri(),
                        'author_id': author_id, 'age_id': age_id})

        connection.commit()
        connection.close()

    def delete(self, book_id: int) -> None:
        connection = sqlite3.connect(config.database['path'])
        cursor = connection.cursor()

        cursor.execute('DELETE FROM book WHERE id = :id', {'id': book_id})

        connection.commit()
        connection.close()

    def list(self) -> List[Book]:
        connection = sqlite3.connect(config.database['path'])
        cursor = connection.cursor()

        cursor.execute('SELECT book.id, title, uri, author.id, author.name, '
                       'age.id, age.name FROM book '
                       'LEFT OUTER JOIN author ON author.id = book.author_id '
                       'LEFT OUTER JOIN age ON age.id = book.age_id ')
        data = cursor.fetchall()

        book_list = []
        for row in data:
            age = Age(row[5], row[6]) if row else None
            author = Author(row[3], row[4]) if row else None
            book_list.append(Book(row[0], row[1], row[2], age, author))

        connection.commit()
        connection.close()

        return book_list

    def list_by_author(self, author: Author) -> List[Book]:
        connection = sqlite3.connect(config.database['path'])
        cursor = connection.cursor()

        cursor.execute('SELECT book.id, title, uri, author.id, author.name, '
                       'age.id, age.name FROM book '
                       'INNER JOIN author ON author.id = book.author_id '
                       'LEFT OUTER JOIN age ON age.id = book.age_id '
                       'WHERE author.name like :title',
                       {'title': '%' + author.get_name() + '%'})
        data = cursor.fetchall()

        book_list = []
        for row in data:
            age = Age(row[5], row[6]) if row else None
            author = Author(row[3], row[4]) if row else None
            book_list.append(Book(row[0], row[1], row[2], age, author))

        connection.commit()
        connection.close()

        return book_list

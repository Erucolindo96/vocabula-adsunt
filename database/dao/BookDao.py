import sqlite3
from typing import List

from config import config
from database.entities.Book import Book
from database.entities.Age import Age


class BookDao:
    def __init__(self):
        pass

    def get_by_id(self, book_id: int) -> Book:
        connection = sqlite3.connect(config.database['path'])
        cursor = connection.cursor()

        cursor.execute('SELECT book.id, title, uri, author, author_slug, '
                       'age.id, age.name, age.slug FROM book '
                       'LEFT OUTER JOIN age ON age.id = book.age_id '
                       'WHERE book.id = :id', {'id': book_id})
        row = cursor.fetchone()

        connection.commit()
        connection.close()
        age = Age(row[5], row[6], row[7]) if row else None

        return Book(book_id=row[0], title=row[1], uri=row[2], age=age,
                    author=row[3],
                    author_slug=row[4]) if row else None

    def list_by_title(self, book_title: str) -> List[Book]:
        connection = sqlite3.connect(config.database['path'])
        cursor = connection.cursor()

        cursor.execute('SELECT book.id, title, uri, author, author_slug, '
                       'age.id, age.name, age.slug FROM book '
                       'LEFT OUTER JOIN age ON age.id = book.age_id '
                       'WHERE book.title like :title',
                       {'title': '%' + book_title + '%'})
        data = cursor.fetchall()

        book_list = []
        for row in data:
            age = Age(row[5], row[6], row[7]) if row else None

            book_list.append(Book(book_id=row[0], title=row[1], uri=row[2],
                                  age=age, author=row[3], author_slug=row[4]))

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
        author_slug = book.get_author_slug()
        age = book.get_age()
        age_id = age.get_id() if age else None

        cursor.execute('INSERT INTO '
                       'book(title, content, uri, author, author_slug, '
                       'age_id) '
                       'VALUES '
                       '(:title, :content, :uri, :author, :author_slug, '
                       ':age_id)',
                       {'title': book.get_title(),
                        'content': book.get_content(), 'uri': book.get_uri(),
                        'author': author, 'author_slug': author_slug,
                        'age_id': age_id})

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

        cursor.execute('SELECT book.id, title, uri, author, author_slug, '
                       'age.id, age.name, age.slug FROM book '
                       'LEFT OUTER JOIN age ON age.id = book.age_id ')
        data = cursor.fetchall()

        book_list = []
        for row in data:
            age = Age(row[5], row[6], row[7]) if row else None
            book_list.append(Book(book_id=row[0], title=row[1], uri=row[2],
                                  age=age, author=row[3], author_slug=row[4]))

        connection.commit()
        connection.close()

        return book_list

    def list_by_author_name(self, author_name: str) -> List[Book]:
        connection = sqlite3.connect(config.database['path'])
        cursor = connection.cursor()

        cursor.execute('SELECT book.id, title, uri, author, author_slug, '
                       'age.id, age.name, age.slug FROM book '
                       'LEFT OUTER JOIN age ON age.id = book.age_id '
                       'WHERE author like :name',
                       {'name': '%' + author_name + '%'})
        data = cursor.fetchall()

        book_list = []
        for row in data:
            age = Age(row[5], row[6], row[7]) if row else None
            book_list.append(Book(book_id=row[0], title=row[1], uri=row[2],
                                  age=age, author=row[3], author_slug=row[4]))

        connection.commit()
        connection.close()

        return book_list

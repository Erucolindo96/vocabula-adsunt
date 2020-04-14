import sqlite3
from typing import List

from config import config
from database.entities.Author import Author


class AuthorDao:
    def __init__(self):
        pass

    def get_by_id(self, author_id: int) -> Author:
        connection = sqlite3.connect(config.database['path'])
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM author WHERE id = :id',
                       {'id': author_id})
        row = cursor.fetchone()

        connection.commit()
        connection.close()

        return Author(row[0], row[1]) if row else None

    def get_by_name(self, author_name: str) -> Author:
        connection = sqlite3.connect(config.database['path'])
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM author WHERE name = :name',
                       {'name': author_name})

        row = cursor.fetchone()

        connection.commit()
        connection.close()

        return Author(row[0], row[1]) if row else None

    def insert(self, author_name: str) -> None:
        connection = sqlite3.connect(config.database['path'])
        cursor = connection.cursor()
        cursor.execute('INSERT INTO author(name) VALUES (:author_name)',
                       {'author_name': author_name})

        connection.commit()
        connection.close()

    def delete(self, author_id: int) -> None:
        connection = sqlite3.connect(config.database['path'])
        cursor = connection.cursor()
        cursor.execute('DELETE FROM author WHERE id = :id', {'id': author_id})

        connection.commit()
        connection.close()

    def list(self) -> List[Author]:
        connection = sqlite3.connect(config.database['path'])
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM author')
        data = cursor.fetchall()

        author_list = []
        for row in data:
            author_list.append(Author(row[0], row[1]))

        connection.commit()
        connection.close()

        return author_list

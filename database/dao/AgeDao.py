import sqlite3
from typing import List

from config import config
from database.entities.Age import Age


class AgeDao:
    def __init__(self):
        pass

    def get_by_id(self, age_id: int) -> Age:
        connection = sqlite3.connect(config.database['path'])
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM age WHERE id = :id', {'id': age_id})
        row = cursor.fetchone()

        connection.commit()
        connection.close()

        return Age(row[0], row[1]) if row else None

    def get_by_name(self, age_name: str) -> Age:
        connection = sqlite3.connect(config.database['path'])
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM age WHERE name = :name',
                       {'name': age_name})

        row = cursor.fetchone()

        connection.commit()
        connection.close()

        return Age(row[0], row[1]) if row else None

    def insert(self, age_name: str) -> None:
        connection = sqlite3.connect(config.database['path'])
        cursor = connection.cursor()
        cursor.execute('INSERT INTO age(name) VALUES (:age_name)',
                       {'age_name': age_name})

        connection.commit()
        connection.close()

    def delete(self, age_id: int) -> None:
        connection = sqlite3.connect(config.database['path'])
        cursor = connection.cursor()
        cursor.execute('DELETE FROM age WHERE id = :id', {'id': age_id})

        connection.commit()
        connection.close()

    def list(self) -> List[Age]:
        connection = sqlite3.connect(config.database['path'])
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM age')
        data = cursor.fetchall()

        age_list = []
        for row in data:
            age_list.append(Age(row[0], row[1]))

        connection.commit()
        connection.close()

        return age_list

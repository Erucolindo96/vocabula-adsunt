import json
import re
import string
import urllib.request
from typing import List

from config import config
from config.config import wolne_lektury
from database.entities.Age import Age
from database.entities.Book import Book
from lecture.wolnelektury.service.TextPreprocessing import TextPreprocessing


class LectureListLoader:
    authors_api = '/api/authors/'

    @staticmethod
    def list_by_author_slug(slug: str) -> List[dict]:
        url = wolne_lektury['host'] + LectureListLoader.authors_api + slug + \
              '/books'
        data = urllib.request.urlopen(url)
        data = data.read()
        return json.loads(data.decode())

    @staticmethod
    def get_details(href: str) -> dict:
        data = urllib.request.urlopen(href).read()
        return json.loads(data.decode())

    @staticmethod
    def get_content(lecture_details: dict):
        if lecture_details['children']:
            return None

        return urllib.request.urlopen(lecture_details['txt']).read().decode()

    @staticmethod
    def get_text_only_from_lecture(mess: str) -> List[str]:
        stopwords = config.lekser['stopwords']

        get_foot = False
        foot_part = []

        nopunc = [char for char in mess if
                  char not in string.punctuation and char not in ['—', '…', '„', '”', '«', '»']]
        nopunc = TextPreprocessing.only_normal_e(nopunc)
        nopunc = ''.join(nopunc)
        nopunc = [word.lower() for word in nopunc.split() if word.lower() not in stopwords]

        # usuwanie ISBN
        if "isbn" in nopunc[:100]:
            nopunc.remove("isbn")
            # usuwanie numeru
        for x in nopunc[:100]:
            if re.match(r'\d{13}', x):
                nopunc.remove(x)

        # pętla wyłapująca stopkę na końcu tekstów z Wolnych Lektur
        for idx, word in enumerate(nopunc):
            if word == 'lektura' and nopunc[idx + 1] == 'podobnie':
                get_foot = True
            if get_foot == True:
                foot_part.append(word)

        # funkcja zwraca oczyszczony tekst pomniejszony o tę stopkę:
        nopunc = ' '.join(nopunc[:-len(foot_part)])
        return nopunc

    @staticmethod
    def create_book(details: dict, content: str, href: str):
        title = details['title']
        author_name = details['authors'][0]['name']
        a_slug = details['authors'][0]['slug']
        b = Book(book_id=None, title=title, uri=href, age=None,
                 author=author_name, author_slug=a_slug)
        b.set_content(content)
        return b

    @staticmethod
    def create_age(details: dict) -> Age:
        name = details['epochs'][0]['name']
        slug = details['epochs'][0]['slug']
        return Age(age_id=None, name=name, slug=slug)

    @staticmethod
    def check_is_polish(details: dict):
        if len(details['translators']) != 0:
            raise LectureTranslatedException(details['title'])


class LectureTranslatedException(BaseException):
    def __init__(self, lecture: str):
        self.__l = lecture

    def get_lecture(self) -> str:
        return self.__l

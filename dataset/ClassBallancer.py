import random
from typing import List

from database.dao.BookDao import BookDao


class ClassBallancer:

    def __init__(self, age_slugs: List[str]):
        self.__age_slugs = age_slugs
        self.__book_ids_per_age = {}
        self.__dao = BookDao()

    def ballance(self):
        min_class = self.__get_min_class()
        for age_slug in self.__age_slugs:
            self.__book_ids_per_age[age_slug] = self.__get_ballanced_ids_for_class(age_slug=age_slug,
                                                                                   min_class=min_class)

    def get_book_ids_of_age(self, age_slug: str):
        return self.__book_ids_per_age[age_slug]

    def __get_min_class(self) -> (str, int):
        ages_words = self.__dao.list_ages_words()
        min_age_with_words = min(ages_words.items(), key=lambda x: x[1])
        return min_age_with_words

    def __get_ballanced_ids_for_class(self, age_slug, min_class) -> List[int]:
        book_ids = self.__dao.list_ids_by_age_slug(age_slug=age_slug)
        if age_slug == min_class[0]:
            return book_ids

        id_to_words = self.__dao.get_content_words_count_for_ids(book_ids)

        random.shuffle(book_ids)
        class_size = 0
        class_book_ids = []
        for id in book_ids:
            if class_size >= min_class[1]:
                break
            class_book_ids.append(id)
            class_size += id_to_words[id]

        return class_book_ids

import random
from typing import List, Dict

from config import config
from config.config import classification
from database.dao.BookDao import BookDao


class ClassBallancer:

    def __init__(self, age_slugs: List[str]):
        self.__age_slugs = age_slugs
        self.__book_ids_per_age = {}
        self.__dao = BookDao()
        self.__age_slugs = classification['age-slugs']

    def ballance(self):

        if config.classification['ballance_class'] is True:
            min_class = self.__get_min_class(age_slugs=self.__age_slugs)
            for age_slug in self.__age_slugs:
                self.__book_ids_per_age[age_slug] = self.__get_ballanced_ids_for_class(age_slug=age_slug,
                                                                                       min_class=min_class)
        else:
            for slug in self.__age_slugs:
                self.__book_ids_per_age[slug] = self.__get_all_ids_for_class(age_slug=slug)

    def get_book_ids_of_age(self, age_slug: str) -> List[int]:
        return self.__book_ids_per_age[age_slug]

    def get_book_ids_per_age(self) -> Dict[str, List[int]]:
        return self.__book_ids_per_age

    def __get_min_class(self, age_slugs) -> (str, int):
        ages_words = self.__dao.list_ages_words()
        ages_words = {key: ages_words[key] for key in age_slugs}
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
            if class_size >= min_class[1] or class_size >= config.classification['max-class-size']:
                break
            class_book_ids.append(id)
            class_size += id_to_words[id]

        return class_book_ids

    def __get_all_ids_for_class(self, age_slug) -> List[int]:
        return self.__dao.list_ids_by_age_slug(age_slug=age_slug)

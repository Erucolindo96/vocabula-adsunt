from typing import List, Dict

from sklearn.model_selection import train_test_split


class TrainTestSplitter:

    def __init__(self, book_id_per_age_slug: Dict[str, List[int]], test_prop: float):
        self.__book_id_per_age_slug = book_id_per_age_slug
        self.__training_set = {}
        self.__test_set = {}
        self.__test_prop = test_prop

    def split_set(self):
        for slug in self.__book_id_per_age_slug.keys():
            train, test = train_test_split(self.__book_id_per_age_slug[slug], test_size=self.__test_prop)
            self.__training_set[slug] = train
            self.__test_set[slug] = test

    def get_training_book_ids_per_class(self, age_slug: str) -> List[int]:
        return self.__training_set[age_slug]

    def get_test_book_ids_per_class(self, age_slug: str) -> List[int]:
        return self.__test_set[age_slug]

    def get_training_book_ids(self) -> Dict[str, List[int]]:
        return self.__training_set

    def get_test_book_ids(self) -> Dict[str, List[int]]:
        return self.__test_set

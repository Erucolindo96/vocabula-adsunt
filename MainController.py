import logging

from classifier.ClassificationProcesor import ClassificationProcesor
from config import config
from database.dao.AgeDao import AgeDao
from database.dao.BookDao import BookDao
from dataset.ClassBallancer import ClassBallancer
from dataset.TrainTestSplitter import TrainTestSplitter
from lecture.wolnelektury.service.WolneLekturyService import WolneLekturyService


class MainController:

    def __init__(self):
        self.__b_dao = BookDao()
        self.__a_dao = AgeDao()
        self.__tested_ages = config.classification['age-slugs']
        self.__test_percent = config.classification['test_size']

    def load_lectures(self):

        all_author_slugs = config.wolne_lektury['author-slugs']

        author_slugs = [all_author_slugs[i] for i in config.wolne_lektury['author-part'] if i < len(all_author_slugs)]

        for slug in author_slugs:
            WolneLekturyService.load_lecture_by_author_slug(slug)

    def learn_and_test_classification(self):
        # wez zrownowazone idki klas
        ballancer = self.__ballancing()

        # utworz zbiory testowe i uczace
        splitter = TrainTestSplitter(book_id_per_age_slug=ballancer.get_book_ids_per_age(),
                                     test_prop=self.__test_percent)
        splitter.split_set()

        # uczenie i test
        classification_proc = ClassificationProcesor()
        classification_proc.load_training_set(splitter.get_training_book_ids())
        classification_proc.load_test_set(splitter.get_test_book_ids())
        classification_proc.trainClassifier()
        classification_proc.testClassifier()

    def delete_content(self):

        ids = (b.get_id() for b in self.__b_dao.list())
        for iden in ids:
            self.__b_dao.delete(book_id=iden)

        a_ids = (a.get_id() for a in self.__a_dao.list())
        for iden in a_ids:
            self.__a_dao.delete(age_id=iden)

    def __ballancing(self) -> ClassBallancer:
        ballancer = ClassBallancer(self.__tested_ages)
        try:
            ballancer.ballance()
        except:
            logging.error('Błąd podczas równoważenia klas')
            raise RuntimeError()

        logging.info('Klasy zrównoważone')

        book_ids_per_class = ballancer.get_book_ids_per_age()

        for age in book_ids_per_class.keys():
            words = sum(self.__b_dao.get_content_words_count_for_ids(book_ids_per_class[age]).values())
            logging.debug('Wielkośc klasy {}: {} słów'.format(age, words))

        return ballancer

import logging

from MainController import MainController
from config import config


def main():
    main_service = MainController()
    if config.task['is_loading_content'] is True:
        main_service.load_lectures()

    if config.task['is_test'] is True:
        main_service.learn_and_test_classification()

    if config.task['delete_content'] is True:
        main_service.delete_content()

    logging.info('Git? Nie, svn')


if __name__ == "__main__":
    main()

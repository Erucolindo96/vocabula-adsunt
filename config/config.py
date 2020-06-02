import logging

from config import Logs
from config.ResourceManager import ResourceManager

task = {
    'is_test': True,
    'is_loading_content': False,
    'delete_content': False
}

classification = {
    'test_size': 0.2,
    'age-slugs': ['dwudziestolecie-miedzywojenne', 'barok', 'romantyzm', 'pozytywizm', 'modernizm'],
    'max-class-size': 50000,
    'ballance_class': False
}

path = {
    "prefix": "/home/krzysztof/Dokumenty/WEDT/vocabulae-adsunt"
}

database = {
    'path': path['prefix'] + '/database/vocabulae.db',
    'name': 'vocabulae.db',
}

wolne_lektury = {
    'host': 'https://wolnelektury.pl',
    'author_slugs_path': path['prefix'] + '/resources/list_of_slugs.txt',
    'author-slugs': [],
    'author-part': range(40, 80)

}

lekser = {
    'stopwords-path': path['prefix'] + '/resources/polish-stopwords.txt',
    'stopwords': []
}

logs = {
    'level': logging.DEBUG
}


def create_config():
    lekser['stopwords'] = ResourceManager.stopwords(lekser['stopwords-path'])
    wolne_lektury['author-slugs'] = ResourceManager.authors_slugs(wolne_lektury['author_slugs_path'])
    Logs.setLogLevel()


create_config()

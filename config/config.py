

database = {
    'path': 'database/vocabulae.db',
    'name': 'vocabulae.db',
    }
wolne_lektury = {
    'host': 'https://wolnelektury.pl',
    }
lekser = {
    'stopwords-path': '/home/erucolindo/Dokumenty/Projekty/Python/'
                      'vocabula-adsunt/resources/polish-stopwords.txt',
    'stopwords': []
    }

with open(lekser['stopwords-path'],
          encoding='utf-8') as f:
    lekser['stopwords'] = f.read()



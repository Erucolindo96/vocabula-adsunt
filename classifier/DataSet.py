from database.dao.BookDao import *

class DataSet:

    def __init__(self):
        self.dao = BookDao()
        self.dataSet = {}

    def load_content(self, dataSet):
        failed_loadings = []
        ages_dictionary = {}
        for age in dataSet:
            ages_dictionary[age] = []
            for id in dataSet[age]:
                try:
                    book = self.dao.get_by_id(id)
                    self.dao.fetch_content(book)
                    ages_dictionary[age].append(book.get_content())
                except:
                    failed_loadings.append(id)
        if len(failed_loadings)!=0:
            print("Nie udało się poprawnie załadować: ", failed_loadings, " książek")
        self.dataSet = ages_dictionary


                
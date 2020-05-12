import unittest
from TfIdfMatrix import *

testDict = {"class_1": ["ABC", "AAB", "CAB", "CCC"],
            "class_2": ["BBC", "AAA", "AAB"],
            "class_3": ["BBA", "AAA", "BBB", "BCA", "CBA", "BAC", "CAB"],
            "class_4": []}
testUniqueWords = ['ABC AAB CAB CCC', 'BBC AAA AAB', 'BBA AAA BBB BCA CBA BAC CAB', '']

class TfidfMatrixCreatorTests(unittest.TestCase):
    def test_matrix_size(self):
        tf_idf = TfIdfMatrix(testDict)
        self.assertCountEqual(tf_idf.corpus, testUniqueWords)
        self.assertIsNot(tf_idf.TfIdfTable.bba.class_3,  0.0)
        self.assertIsNot(tf_idf.TfIdfTable.aaa.class_2,  tf_idf.TfIdfTable.aab.class_2)
        pass

if __name__ == '__main__':
    unittest.main()

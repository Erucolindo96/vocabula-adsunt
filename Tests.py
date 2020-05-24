import unittest
from TfIdfMatrix import *
from NaiveBayes import *

testDict = {"class_1": ["ABC", "AAB", "CAB", "CCC"],
            "class_2": ["BBC", "AAA", "AAB"],
            "class_3": ["BBA", "AAA", "BBB", "BCA", "CBA", "BAC", "CAB"],
            "class_4": []}
testUniqueWords = ['ABC AAB CAB CCC', 'BBC AAA AAB', 'BBA AAA BBB BCA CBA BAC CAB', '']

textForPrediction = [["BBC", "AAA"], ["BBA", "AAA", "BBB"], ["FFG"]]

class TfidfMatrixCreatorTests(unittest.TestCase):
    def test_matrix_size(self):
        tf_idf = TfIdfMatrix(testDict)
        self.assertCountEqual(tf_idf.corpus, testUniqueWords)
        self.assertEqual(tf_idf.TfIdfTable.ccc.class_3,  0.0)
        self.assertEqual(tf_idf.TfIdfTable.bac.class_1,  0.0)
        self.assertEqual(tf_idf.TfIdfTable.cba.class_2, tf_idf.TfIdfTable.cab.class_2)
        pass
    
    def test_bayes_classifier(self):
        tf_idf = TfIdfMatrix(testDict)
        #print(tf_idf.trainVector.toarray())
        clc = BayesClassifier(tf_idf)
        clc.fit()
        transformedText = tf_idf.transformText(textForPrediction)
        predictedClass = clc.predictClass(transformedText)
        self.assertIs(predictedClass[0], "class_2")
        self.assertIs(predictedClass[1], "class_3")
        print(predictedClass)
        pass

if __name__ == '__main__':
    unittest.main()

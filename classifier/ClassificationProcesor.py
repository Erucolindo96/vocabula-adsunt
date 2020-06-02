from classifier.NaiveBayes import *
from classifier.DataSet import *
import pandas as pd

class ClassificationProcesor:
    def __init__(self):
        self.trainData = DataSet()
        self.testData = DataSet()
        self.trueResult = None
        self.falseResult = None

    def load_training_set(self, trainingSet):
        try:
            self.trainData.load_content(trainingSet)
            print("Dane zostały załadowane poprawnie")
        except:
            print("Błąd przy ładowaniu danych treningowych")

    def load_test_set(self, testSet):
        try:
            self.testData.load_content(testSet)
            print("Dane zostały załadowane poprawnie")
        except:
            print("Błąd przy ładowaniu danych testowych")

    def trainClassifier(self):
        self.tf_idf = TfIdfMatrix(self.trainData.dataSet)
        self.clc = BayesClassifier(self.tf_idf)
        self.clc.fit()

    def deleteTrainSet(self):
        del self.trainData

    def testClassifier(self):
        self.trueResult = 0
        self.falseResult = 0
        self.confusionMatrix = pd.DataFrame(0, index = self.tf_idf.labels,  columns=self.tf_idf.labels)
        for age in self.testData.dataSet:
            transformedText = self.tf_idf.transformText(self.testData.dataSet[age])
            predictedClass = self.clc.predictClass(transformedText)
            for result in predictedClass:
                self.confusionMatrix[result][age] += 1
                if result == age:
                    self.trueResult += 1
                else:
                    self.falseResult += 1
        trueResultPercent = (self.trueResult)/(self.trueResult+self.falseResult)*100
        falseResultPercent = (self.falseResult)/(self.trueResult+self.falseResult)*100
        print("Procent poprawnych odpowiedzi klasyfikatora: ", trueResultPercent, "%")
        print("Procent niepoprawnych odpowiedzi klasyfikatora: ", falseResultPercent, "%")
        print("Macierz pomyłek: \n", self.confusionMatrix)

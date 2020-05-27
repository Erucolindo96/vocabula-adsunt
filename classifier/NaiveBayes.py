from sklearn.naive_bayes import MultinomialNB
from classifier.TfIdfMatrix import *

class BayesClassifier:
    def __init__(self, TfIdfTable):
        self.trainingData = TfIdfTable
        self.NaiveBayesClassifier = MultinomialNB()
        self.labelsNumbers = self.__setLabelsNumbers(TfIdfTable.labels)

    def fit(self):
        self.NaiveBayesClassifier.fit(self.trainingData.trainVector, self.labelsNumbers)

    def __setLabelsNumbers(self, classLabels):
        labelsNumbers = []
        for i in range(len(classLabels)):
            labelsNumbers.append(i)
        return labelsNumbers

    def predictClass(self, transformedText):
        predictedClass = self.NaiveBayesClassifier.predict(transformedText)
        predictedClass = predictedClass.astype('int')
        className = []
        for c in predictedClass:
            className.append(self.trainingData.labels[c])
        return className
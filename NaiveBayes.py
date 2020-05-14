from sklearn.naive_bayes import MultinomialNB
from TfIdfMatrix import *

class BayesClassifier:
    def __init__(self, TfIdfTable):
        self.trainingData = TfIdfTable
        self.NaiveBayesClassifier = MultinomialNB()
        self.labelsNumbers = self.setLabelsNumbers(TfIdfTable.labels)
        self.NaiveBayesClassifier.fit(TfIdfTable.trainVector, self.labelsNumbers)

    def setLabelsNumbers(self, classLabels):
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
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import numpy as np

class TfIdfMatrix:
    def __init__(self, bagOfWordsSet):
        self.vec = TfidfVectorizer()
        self.corpus = self.transformSetForVectorizer(bagOfWordsSet)
        self.labels = self.getLabels(bagOfWordsSet)
        [self.TfIdfTable, self.trainVector] = self.computeTfIdfTable()

    def transformSetForVectorizer(self, bagOfWordsSet):
        corpus = {}
        for c in bagOfWordsSet:
            corpus[c] = " ".join(bagOfWordsSet[c])
        corpus = list(corpus.values())
        return corpus
    
    def getLabels(self, bagOfWordsSet):
        labels = list(bagOfWordsSet)
        return labels

    def computeTfIdfTable(self):
        vectors = self.vec.fit_transform(self.corpus)
        feature_names = self.vec.get_feature_names()
        dense = vectors.todense()
        denselist = dense.tolist()
        TfIdfTable = pd.DataFrame(denselist, columns=feature_names, index=self.labels)
        return TfIdfTable, vectors

    def transformText(self, text):
        joinedText = []
        for t in text:
            joinedText.append(" ".join(t))
        transformedText = self.vec.transform(joinedText)
        return transformedText
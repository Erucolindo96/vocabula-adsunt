from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import numpy as np

class TfIdfMatrix:
    def __init__(self, bagOfWordsSet):
        self.vec = TfidfVectorizer()
        self.corpus = self.__transformSetForVectorizer(bagOfWordsSet)
        self.labels = self.__getLabels(bagOfWordsSet)
        [self.TfIdfTable, self.trainVector] = self.__computeTfIdfTable()

    def __transformSetForVectorizer(self, bagOfWordsSet):
        corpus = {}
        for c in bagOfWordsSet:
            corpus[c] = " ".join(bagOfWordsSet[c])
        corpus = list(corpus.values())
        return corpus
    
    def __getLabels(self, bagOfWordsSet):
        labels = list(bagOfWordsSet)
        return labels

    def __computeTfIdfTable(self):
        vectors = self.vec.fit_transform(self.corpus)
        feature_names = self.vec.get_feature_names()
        dense = vectors.todense()
        denselist = dense.tolist()
        TfIdfTable = pd.DataFrame(denselist, columns=feature_names, index=self.labels)
        return TfIdfTable, vectors

    def transformText(self, texts):
        transformedTexts = self.vec.transform(texts)
        return transformedTexts
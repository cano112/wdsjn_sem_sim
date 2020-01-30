import itertools
from collections import Counter

from core.common.SemanticSimilarityAlgorithm import SemanticSimilarityAlgorithm

import numpy as np


class SifCosineSimilarity(SemanticSimilarityAlgorithm):

    def get_label(self):
        return "Smooth Inverse Frequency + Cosine Distance"

    def __init__(self, embedding, stemmer):
        super().__init__()
        self.a = 0.001
        self.embedding = embedding
        self.stemmer = stemmer

    def _absolute_score(self, sentence_1, sentence_2):
        splitted_1 = self.stemmer.stem_sentence(sentence_1)
        splitted_2 = self.stemmer.stem_sentence(sentence_2)
        vecs = self._sif_feature_vectors(splitted_1, splitted_2, self.embedding)
        A = vecs[0]
        B = vecs[1]
        return A @ B / (np.linalg.norm(A) * np.linalg.norm(B))

    def _normalize(self, absolute):
        return absolute * 50 + 50

    # Based on
    # medium.com/@Intellica.AI/comparison-of-different-word-embeddings-on-text-similarity-a-use-case-in-nlp-e83e08469c1c
    def _sif_feature_vectors(self, splitted_1, splitted_2, embedding, a=0.001):
        s_1 = [token for token in splitted_1 if token in embedding.model.wv.vocab]
        s_2 = [token for token in splitted_2 if token in embedding.model.wv.vocab]
        word_counts = self._map_word_frequency((s_1 + s_2))
        sentence_set = []
        for sentence in [s_1, s_2]:
            vs = np.zeros(embedding.model_shape)
            sentence_length = len(sentence)
            for word in sentence:
                a_value = a / (a + word_counts[word])  # smooth inverse frequency, SIF
                vs = np.add(vs, np.multiply(a_value, embedding.model.wv[word]))  # vs += sif * word_vector
            vs = np.divide(vs, sentence_length)  # weighted average
            sentence_set.append(vs)
        return sentence_set

    def _map_word_frequency(self, document):
        return Counter(itertools.chain(*document))


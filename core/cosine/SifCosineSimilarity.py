
from core.common.SemanticSimilarityAlgorithm import SemanticSimilarityAlgorithm
from core.common.utils import preprocess, sif_feature_vectors

import numpy as np


class SifCosineSimilarity(SemanticSimilarityAlgorithm):

    def get_label(self):
        return "Smooth Inverse Frequency + Cosine Distance"

    def __init__(self, embedding):
        super().__init__()
        self.a = 0.001
        self.embedding = embedding

    def _absolute_score(self, sentence_1, sentence_2):
        splitted_1 = preprocess(sentence_1)
        splitted_2 = preprocess(sentence_2)
        vecs = sif_feature_vectors(splitted_1, splitted_2, self.embedding)
        A = vecs[0]
        B = vecs[1]
        return A @ B / (np.linalg.norm(A) * np.linalg.norm(B))

    def _normalize(self, absolute):
        return absolute * 50 + 50

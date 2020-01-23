import numpy as np

from core.common.SemanticSimilarityAlgorithm import SemanticSimilarityAlgorithm


class CustomEnsembleSimilarity(SemanticSimilarityAlgorithm):

    def get_label(self):
        return "Custom Ensembled Similarity"

    def __init__(self, algos):
        super().__init__()
        self.algos = algos

    def _absolute_score(self, sentence_1, sentence_2):
        return np.average(
            [algo.normalized_score(sentence_1, sentence_2) for algo, weight in self.algos],
            weights=[weight for algo, weight in self.algos])

    def _normalize(self, absolute):
        return absolute

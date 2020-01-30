import numpy as np

from core.common.SemanticSimilarityAlgorithm import SemanticSimilarityAlgorithm


class CosineSimilarity(SemanticSimilarityAlgorithm):

    def get_label(self):
        return "Cosine Distance"

    def __init__(self, embedding, stemmer):
        super().__init__()
        self.embedding = embedding
        self.stemmer = stemmer

    def _absolute_score(self, sentence_1, sentence_2):
        splitted_1 = self.stemmer.stem_sentence(sentence_1)
        splitted_2 = self.stemmer.stem_sentence(sentence_2)
        A = self._calculate_mean_vector(splitted_1)
        B = self._calculate_mean_vector(splitted_2)
        return A @ B / (np.linalg.norm(A) * np.linalg.norm(B))

    def _calculate_mean_vector(self, splitted):
        vectors = []
        vocab = self.embedding.model.vocab
        for word in splitted:
            if word in vocab:
                vectors.append(self.embedding.model.get_vector(word))
            elif word.capitalize() in vocab:
                vectors.append(self.embedding.model.get_vector(word.capitalize()))
            else:
                print('Słowa "{}" nie znaleziono w słowniku, więc zostało pominięte.'.format(word))
        return np.mean(vectors, axis=0)

    def _normalize(self, absolute):
        return absolute * 50 + 50

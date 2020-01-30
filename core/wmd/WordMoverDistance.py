from core.common.SemanticSimilarityAlgorithm import SemanticSimilarityAlgorithm


class WordMoverDistance(SemanticSimilarityAlgorithm):

    def get_label(self):
        return "Word Mover Distance"

    def __init__(self, embedding, stemmer):
        super().__init__()
        self.embedding = embedding
        self.stemmer = stemmer

    def _absolute_score(self, sentence_1, sentence_2):
        splitted_1 = self.stemmer.stem_sentence(sentence_1)
        splitted_2 = self.stemmer.stem_sentence(sentence_2)
        return self.embedding.model.wmdistance(splitted_1, splitted_2)

    def _normalize(self, absolute):
        # We assume that max distance is 1.5
        # TODO: come up with better normalization
        normalized = -(absolute * 200 / 3) + 100
        return min(normalized, 100)

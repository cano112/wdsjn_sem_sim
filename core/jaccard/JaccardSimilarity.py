from core.common.SemanticSimilarityAlgorithm import SemanticSimilarityAlgorithm


class JaccardSimilarity(SemanticSimilarityAlgorithm):

    def get_label(self):
        return "Jaccard Similarity";

    def __init__(self, stemmer):
        super().__init__()
        self.stemmer = stemmer

    def _absolute_score(self, sentence_1, sentence_2):
        stemmed_1 = self.stemmer.stem_sentence(sentence_1)
        stemmed_2 = self.stemmer.stem_sentence(sentence_2)
        intersection = stemmed_1.intersection(stemmed_2)
        union = stemmed_1.union(stemmed_2)
        return len(intersection) / len(union)

    def _normalize(self, absolute):
        return absolute * 100

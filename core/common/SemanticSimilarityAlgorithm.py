from abc import abstractmethod


class SemanticSimilarityAlgorithm:

    def __init__(self):
        super().__init__()

    @abstractmethod
    def get_label(self):
        pass

    @abstractmethod
    def _absolute_score(self, sentence_1, sentence_2):
        pass

    @abstractmethod
    def _normalize(self, absolute):
        pass

    def absolute_score(self, sentence_1, sentence_2):
        self._log_invocation()
        return self._absolute_score(sentence_1, sentence_2)

    def normalized_score(self, sentence_1, sentence_2):
        self._log_invocation()
        return self._normalize(self._absolute_score(sentence_1, sentence_2))

    def _log_invocation(self):
        print("Liczę używając algorytmu {}".format(self.__class__.__name__))

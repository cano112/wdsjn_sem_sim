import string
import itertools

import numpy as np
from stempel import StempelStemmer
from collections import Counter

punct_translator = str.maketrans('', '', string.punctuation)

stemmer = StempelStemmer.polimorf()


def remove_punct(sentence):
    return sentence.translate(punct_translator)


def stem(sentence):
    res = set()
    for word in sentence.split():
        res.add(stemmer.stem(word))
    return res


def preprocess(sentence):
    return stem(remove_punct(sentence.lower()))


# Based on
# medium.com/@Intellica.AI/comparison-of-different-word-embeddings-on-text-similarity-a-use-case-in-nlp-e83e08469c1c
def sif_feature_vectors(splitted_1, splitted_2, embedding, a=0.001):
    s_1 = [token for token in splitted_1 if token in embedding.model.wv.vocab]
    s_2 = [token for token in splitted_2 if token in embedding.model.wv.vocab]
    word_counts = _map_word_frequency((s_1 + s_2))
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


def _map_word_frequency(document):
    return Counter(itertools.chain(*document))

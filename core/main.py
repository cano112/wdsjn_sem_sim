from core.config import Algorithm, stemmer_path
from core.config import embedding_path, embedding_shape, get_algorithms
from core.embeddings.EmbeddingModelWrapper import EmbeddingModelWrapper

import argparse

from core.stemmer.SgjpStemmer import SgjpStemmer


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("sentence1", help='Pierwsze zdanie do porównania.', type=str)
    parser.add_argument("sentence2", help='Drugie zdanie do porównania.', type=str)
    parser.add_argument("-a", "--algorithm", help="Użyty algorytm (jeden z: {})".format([a.name for a in Algorithm]),
                        type=str, default=Algorithm.jaccard.name)
    parser.add_argument("-e", "--embedding", help="Ścieżka do pliku z modelem word2vec.",
                        type=str, default=embedding_path)
    args = parser.parse_args()

    embedding = EmbeddingModelWrapper(args.embedding, embedding_shape)
    stemmer = SgjpStemmer(stemmer_path)
    algorithms = get_algorithms(embedding, stemmer)
    result = algorithms[args.algorithm].normalized_score(args.sentence1, args.sentence2)

    print("Zdanie 1: {}".format(args.sentence1))
    print("Zdanie 2: {}".format(args.sentence2))
    print("Indeks podobieństwa: {}%".format(result))


if __name__ == "__main__":
    main()

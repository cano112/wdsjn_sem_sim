from enum import Enum

from core.cosine.CosineSimilarity import CosineSimilarity
from core.cosine.SifCosineSimilarity import SifCosineSimilarity
from core.ensembled.CustomEnsembleSimilarity import CustomEnsembleSimilarity
from core.jaccard.JaccardSimilarity import JaccardSimilarity
from core.wmd.WordMoverDistance import WordMoverDistance

embedding_path, embedding_shape = "embeddings/nkjp+wiki-lemmas-all-300-cbow-hs.txt", 300

stemmer_path = 'stemmer/sgjp-20190303.tab'

class Algorithm(Enum):
    jaccard = 1
    wmd = 2
    cosine = 3
    sif_cosine = 4
    ensemble = 5


def get_algorithms(embedding, stemmer):
    return {
        Algorithm.jaccard.name: JaccardSimilarity(stemmer),
        Algorithm.wmd.name: WordMoverDistance(embedding, stemmer),
        Algorithm.cosine.name: CosineSimilarity(embedding, stemmer),
        Algorithm.sif_cosine.name: SifCosineSimilarity(embedding, stemmer),
        Algorithm.ensemble.name: CustomEnsembleSimilarity([
            (SifCosineSimilarity(embedding, stemmer), 0.3),
            (WordMoverDistance(embedding, stemmer), 0.6)
        ])
    }

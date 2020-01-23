from enum import Enum

from core.cosine.CosineSimilarity import CosineSimilarity
from core.cosine.SifCosineSimilarity import SifCosineSimilarity
from core.ensembled.CustomEnsembleSimilarity import CustomEnsembleSimilarity
from core.jaccard.JaccardSimilarity import JaccardSimilarity
from core.wmd.WordMoverDistance import WordMoverDistance

embedding_path, embedding_shape = "embeddings/nkjp+wiki-lemmas-all-300-cbow-hs.txt", 300


class Algorithm(Enum):
    jaccard = 1
    wmd = 2
    cosine = 3
    sif_cosine = 4
    ensemble = 5


def get_algorithms(embedding):
    return {
        Algorithm.jaccard.name: JaccardSimilarity(),
        Algorithm.wmd.name: WordMoverDistance(embedding),
        Algorithm.cosine.name: CosineSimilarity(embedding),
        Algorithm.sif_cosine.name: SifCosineSimilarity(embedding),
        Algorithm.ensemble.name: CustomEnsembleSimilarity([
            (SifCosineSimilarity(embedding), 0.3),
            (WordMoverDistance(embedding), 0.6)
        ])
    }


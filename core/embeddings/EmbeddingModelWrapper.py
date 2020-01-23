import os
from gensim.models import KeyedVectors


class EmbeddingModelWrapper:

    def __init__(self, path, shape):
        super().__init__()
        vector_path = path.split(".")[0] + "_precomputed"
        self.model_shape = shape
        if os.path.isfile(vector_path):
            self.model = KeyedVectors.load(vector_path, mmap='r')
        else:
            self.model = KeyedVectors.load_word2vec_format(path, binary=False)
            self.model.init_sims(replace=True)
            self.model.save(vector_path)

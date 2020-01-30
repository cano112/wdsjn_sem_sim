from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

from core.config import embedding_path, embedding_shape, get_algorithms, stemmer_path
from core.embeddings.EmbeddingModelWrapper import EmbeddingModelWrapper
from core.stemmer.SgjpStemmer import SgjpStemmer

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

embedding = EmbeddingModelWrapper(embedding_path, embedding_shape)

stemmer = SgjpStemmer(stemmer_path)


@app.route("/similarity", methods=["GET"])
@cross_origin()
def get_similarity():
    algorithm_names = request.args['algorithms'].split(",")
    sentence_1 = request.args['s1']
    sentence_2 = request.args['s2']
    algorithms = get_algorithms(embedding, stemmer)
    data = [['Algorithm', "Value"]]
    data.extend(
        [[algorithms[name].get_label(),
          round(algorithms[name].normalized_score(sentence_1, sentence_2), 2)] for name in algorithm_names])
    return jsonify(data), 200


if __name__ == '__main__':
    #app.run(host='0.0.0.0')
    app.run()

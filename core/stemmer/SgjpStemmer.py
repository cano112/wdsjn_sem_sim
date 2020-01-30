import string


class SgjpStemmer:

    def __init__(self, dict_path) -> None:
        self.words = self._load_dict(dict_path)
        self.punct_translator = str.maketrans('', '', string.punctuation)

    def _load_dict(self, dict_path):
        words = {}
        with open(dict_path, 'r') as d:
            lines = d.readlines()
            for line in lines[29:]:
                splitted = line.split('	')
                words[splitted[0]] = splitted[1].split(':')[0]
        return words

    def stem(self, word):
        return self.words[word]

    def stem_sentence(self, sentence):
        processed = self._remove_punct(sentence.lower())
        res = set()
        for word in processed.split():
            res.add(self.stem(word))
        return res

    def _remove_punct(self, sentence):
        return sentence.translate(self.punct_translator)

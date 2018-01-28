#!/usr/bin/env python

import json
from gensim.models import word2vec

from underlines.common import config
import __root__

STOPWORDS = json.load(open(__root__.path() + '/resources/stopwords.json', 'rt', encoding='utf-8'))
VAILD_POS = ("Noun", "Adjective", "Verb")
MODEL_PATH = __root__.path() + config.get("MODEL_PATH")

class Rodriguez:
    def __init__(self):
        self.model = load()

    def train(self, sentences):
        list_of_tokens = _tokenize(sentences)
        total_words = sum(len(tokens) for tokens in list_of_tokens)
        self.model.train(list_of_tokens, total_examples=len(sentences), total_words=total_words, epochs=50)
        self.model.init_sims(replace=True)
        self.model.save(MODEL_PATH)

    def build(self, sentences):
        model = word2vec.Word2Vec(_tokenize(sentences), size=50, window=3, min_count=10, workers=4, iter=10, sg=1)
        model.init_sims(replace=True)
        model.save(MODEL_PATH)
        self.model = model

    def ask(self, keyword):
        return self.model.wv.most_similar(keyword)

    def show_me_your_brain(self):
        for word in self.model.wv.vocab:
            print(word)

def load():
    model = word2vec.Word2Vec.load(MODEL_PATH)
    return model

def _tokenize(sentences):
    from konlpy.tag import Twitter
    twitter = Twitter()
    pos = lambda sentence: [token[0] for token in twitter.pos(sentence, True, True) if _is_valid_token(token)]
    tokens = [pos(sentence) for sentence in sentences]
    return tokens

def _is_valid_token(token):
    return (token[1].endswith(VAILD_POS)) and token[0] not in STOPWORDS

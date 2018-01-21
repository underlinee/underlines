#!/usr/bin/env python
import json

from os import path
from gensim.models import word2vec

STOPWORDS = json.load(open('../../resources/stopwords.json', 'rt', encoding='utf-8'))
VAILD_POS = ("Noun", "Adjective", "Verb")
MODEL_PATH='../../resources/underlines.model'

def train(txts):
    if path.exists(MODEL_PATH):
        model = word2vec.Word2Vec.load(MODEL_PATH)
        model.init_sims(replace=True)
        model.save(MODEL_PATH)
    else:
        create_model(txts)

def create_model(txts):
    model = word2vec.Word2Vec(_tokenize(txts), size=50, window=2, min_count=1, workers=4, iter=100, sg=1)
    model.init_sims(replace=True)
    model.save(MODEL_PATH)

def _tokenize(txts):
    from konlpy.tag import Twitter
    twitter = Twitter()
    pos = lambda txt: ['/'.join(token) for token in twitter.pos(txt, True, True) if _is_valid_token(token)]
    tokens = [pos(txt) for txt in txts]
    return tokens

def _is_valid_token(token):
    return (token[1].endswith(VAILD_POS)) and token[0] not in STOPWORDS

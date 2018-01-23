#!/usr/bin/env python

import json
from gensim.models import word2vec

from underlines.common import config

STOPWORDS = json.load(open('../../resources/stopwords.json', 'rt', encoding='utf-8'))
VAILD_POS = ("Noun", "Adjective", "Verb")
MODEL_PATH = config.get("MODEL_PATH")

def train(sentences):
    model = word2vec.Word2Vec.load(MODEL_PATH)
    list_of_tokens = _tokenize(sentences)
    total_words = sum(len(tokens) for tokens in list_of_tokens)
    model.train(list_of_tokens, total_examples=len(sentences), total_words=total_words, epochs=50)
    model.init_sims(replace=True)
    model.save(MODEL_PATH)

def build(sentences):
    # if not os.path.exists(MODEL_PATH):
    model = word2vec.Word2Vec(_tokenize(sentences), size=100, window=3, min_count=1, workers=4, iter=50, sg=1)
    model.init_sims(replace=True)
    model.save(MODEL_PATH)

def _tokenize(sentences):
    from konlpy.tag import Twitter
    twitter = Twitter()
    pos = lambda sentence: ['/'.join(token) for token in twitter.pos(sentence, True, True) if _is_valid_token(token)]
    tokens = [pos(sentence) for sentence in sentences]
    return tokens

def _is_valid_token(token):
    return (token[1].endswith(VAILD_POS)) and token[0] not in STOPWORDS

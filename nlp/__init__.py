"""NLP package for Python

>>> import nlp
>>> nlp.tokenize('Walking on sunshine!')
['walk', 'sunshine']
>>> [nlp.stem(word) for word in ['works', 'working', 'work']]
['work', 'work', 'work']
"""


import re

from .stop_words import stop_words

__version__ = '0.1.0'


def stem(word):
    """Stem a word

    >>> stem('working')
    'work'
    >>> stem('works')
    'work'
    """
    return re.sub(r'(s|ing)$', '', word)


def tokenize(text):
    tokens = []
    for tok in re.findall('[a-zA-Z]+', text):
        tok = tok.lower()
        tok = stem(tok)
        if tok and tok not in stop_words:
            tokens.append(tok)
    return tokens

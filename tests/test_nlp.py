import pytest
from hypothesis import given
from hypothesis.strategies import text, builds, integers
from dataclasses import dataclass

import nlp


def test_smoke():
    pass


def test_tokenize():
    text = "Who's on first?"
    out = nlp.tokenize(text)
    expected = ['first']
    assert out == expected, 'bad tokenize'


tokenize_cases = [
    ("Who's on first?", ['first']),
    ("What's on second", ['second']),
    ('', []),
]


@pytest.mark.parametrize('text, expected', tokenize_cases)
def test_tokenize_many(text, expected):
    out = nlp.tokenize(text)
    assert out == expected, 'bad tokenize'


def test_bad_type():
    with pytest.raises(TypeError):
        nlp.tokenize(b'How are you?')


@given(text())
def test_random(text):
    # print(text)  # MT: -s
    tokens = nlp.tokenize(text)
    assert len(tokens) <= len(text), 'bad tokenize'


@dataclass
class User:
    name: str
    id: int


users = builds(User, text(), integers())


@given(users)
def test_user(user):
    # print(user)
    pass

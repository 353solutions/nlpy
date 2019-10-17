import pytest
from nlp import sentences


test_cases = [
    ('How are you? I am fine.', ['How are you?', 'I am fine.']),
    ('', []),
    ("Who's on first? What's on second",
        ["Who's on first?", "What's on second"]),
]


@pytest.mark.parametrize('text, expected', test_cases)
def test_sentencize(text, expected):
    out = list(sentences.sentencize(text))
    assert out == expected, text

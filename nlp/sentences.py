import re


def sentencize(text):
    """Split text to sentences.

    >>> list(sentencize('How are you? I am fine.'))
    ['How are you?', 'I am fine.']
    """
    start = 0
    for match in re.finditer(r'[.!?]', text):
        yield text[start:match.end()].strip()
        start = match.end()

    # Sentinel
    if start < len(text):
        yield text[start:].strip()

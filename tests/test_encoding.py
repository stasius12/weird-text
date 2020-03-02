import pytest
from collections import Counter

from src.encoding import Encryptor


@pytest.mark.parametrize("word,cant_be_shuffled", [
    ('b', True),
    ('big', True),
    ('biiig', True),
    ('home', False),
    ('aloha', False)
])
def test_shuffle_word(word, cant_be_shuffled):
    b = Encryptor('')
    if cant_be_shuffled:
        assert b._shuffle_word(word) == word
    else:
        assert b._shuffle_word(word) != word


@pytest.mark.parametrize("text,encrypted_words", [
    ('This is really big', ['really', 'This']),
    ('This, is !!! really ## big **,', ['really', 'This']),
    (
        'This is a long looong test sentence,\nwith some big (biiiiig) words!',
        ['long', 'looong', 'sentence', 'some', 'test', 'This', 'with', 'words']
    ),
    (
        'Lets say we have a sentence like that one',
        ['have', 'Lets', 'like', 'sentence', 'that']
    )
])
def test_encode(text, encrypted_words):
    b = Encryptor(text)
    b.encode()
    result = b.result_text.split('\n-weird-\n')[1]
    assert b.encrypted_words == encrypted_words
    for word in encrypted_words:
        assert word not in result
